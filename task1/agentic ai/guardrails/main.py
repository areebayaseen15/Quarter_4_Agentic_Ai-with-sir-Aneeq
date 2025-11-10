import os
from dotenv import load_dotenv
import asyncio
from pydantic import BaseModel
from openai import AsyncOpenAI
from agents import (
    Agent,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    OutputGuardrailTripwireTriggered,
    OpenAIChatCompletionsModel,
    RunContextWrapper,
    Runner,
    TResponseInputItem,
    input_guardrail,
    output_guardrail,
    RunConfig,
)

gemini_api_key = "AIzaSyC7JtvQM1BJCl36Tix55p8e4r95Hc2CSOk"
# Set up Gemini
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Model & Config
model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# --- Input Guardrail ---

class InputGuardrailOutput(BaseModel):
    is_math_homework: bool
    reasoning: str

input_guardrail_agent = Agent(
    name="Input Guardrail Checker",
    instructions="Check if the user is asking for math homework help.",
    output_type=InputGuardrailOutput
)

@input_guardrail
async def math_input_guardrail(
    ctx: RunContextWrapper[None],
    agent: Agent,
    input: str | list[TResponseInputItem],
) -> GuardrailFunctionOutput:
    result = await Runner.run(input_guardrail_agent, input, context=ctx.context, run_config=config)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_math_homework,
    )

# --- Output Guardrail ---

class AgentOutput(BaseModel):
    response: str

class OutputGuardrailCheck(BaseModel):
    is_math: bool
    reasoning: str

output_guardrail_agent = Agent(
    name="Output Guardrail Checker",
    instructions="Check if the response contains math-related answers.",
    output_type=OutputGuardrailCheck,
)

@output_guardrail
async def math_output_guardrail(
    ctx: RunContextWrapper,
    agent: Agent,
    output: AgentOutput,
) -> GuardrailFunctionOutput:
    result = await Runner.run(output_guardrail_agent, output.response, context=ctx.context, run_config=config)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_math,
    )

# --- Main Agent with Both Guardrails ---

agent = Agent(
    name="Customer Support Agent",
    instructions="You are a customer support agent. Help users only with product or service issues.",
    input_guardrails=[math_input_guardrail],
    output_guardrails=[math_output_guardrail],
    output_type=AgentOutput,
)

# --- Test ---

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
