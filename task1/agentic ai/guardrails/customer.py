
import os
from agents.run import RunConfig
from dotenv import load_dotenv
import asyncio
from openai import AsyncOpenAI
from openai.types.responses import ResponseTextDeltaEvent
from agents import (
    Agent,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    OpenAIChatCompletionsModel,
    OutputGuardrailTripwireTriggered,
    RunContextWrapper,
    Runner,
    TResponseInputItem,
    input_guardrail,
    output_guardrail
)

from pydantic import BaseModel

load_dotenv()

gemini_api_key = "AIzaSyC7JtvQM1BJCl36Tix55p8e4r95Hc2CSOk"


external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

class RelevanceCheckOutput(BaseModel):
    is_relevant: bool
    reasoning: str


guardrail_agent = Agent(
    name="Relevance Check",
    instructions=(
        "Determine if the user's input is relevant to customer support. "
        "Respond with is_relevant = False if the input is asking for personal help with homework, jokes, "
        "philosophy, coding, or anything unrelated to product/service support."
    ),
    output_type=RelevanceCheckOutput,
)

@input_guardrail
async def relevance_check_guardrail(
    ctx : RunContextWrapper[None], agent:Agent , input:str | list[TResponseInputItem]
)-> GuardrailFunctionOutput:
    result = await Runner.run(guardrail_agent , input, context=ctx.context , run_config=config)

    return GuardrailFunctionOutput(
        output_info=result.final_output ,
        tripwire_triggered=result.final_output.is_relevant == False,
    )


class AgentOutput(BaseModel):
    response:str


class OutputGuardrailCheck(BaseModel):
    is_relavant:bool
    reasonuing:str

Output_guardrail_agent = Agent(
    name ="Output Guardrail Checker",
    instructions ="Check if the response is relavabnt to the user's querry based on the customer support context.",
    output_type=OutputGuardrailCheck,

)   

@output_guardrail
async def output_guardrail(
    ctx: RunContextWrapper,
    agent: Agent,
    output:AgentOutput,

)->GuardrailFunctionOutput:
    result = await Runner.run(Output_guardrail_agent , output.response , context=ctx.context , run_config=config)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_relavant == False,
    )
agent = Agent(  
    name="Customer support agent",
    instructions="You are a customer support agent. You help customers with their questions.",
    input_guardrails=[relevance_check_guardrail],
    output_guardrails=[output_guardrail],
    output_type=AgentOutput,
)


# This should trip the guardrail

async def main():
    try:
        result = await Runner.run(agent, "Hello, can you help me solve for x: 2x + 3 = 11?", run_config=config)
        print("Guardrail didn't trip - this is unexpected")
        print(result.final_output.response)
    except InputGuardrailTripwireTriggered:
        print("🚫 Input guardrail tripped: math detected in input")
    except OutputGuardrailTripwireTriggered:
        print("🚫 Output guardrail tripped: math detected in output")

    try:
        result = await Runner.run(agent, "Hello, I need help with my billing.", run_config=config)
        print("✅ Valid support query:")
        print(result.final_output.response)
    except Exception as e:
        print("Unexpected exception:", e)

if __name__ == "__main__":
    asyncio.run(main())