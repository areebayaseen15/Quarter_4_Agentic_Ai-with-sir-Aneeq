import asyncio
from agents import Agent , Runner , OpenAIChatCompletionsModel , AsyncOpenAI, handoff , set_tracing_disabled
import os

from dotenv import load_dotenv

# Tracing disabled
set_tracing_disabled(disabled=True)
# llm service
external_client :AsyncOpenAI =AsyncOpenAI(
    api_key="AIzaSyAjPhwuXX3q2jHv8Bg7SBO8btUWteYYW6o",
   base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

BillingAgent=Agent(name = "Billing Agent", instructions="You are a billing agent. You can help customers with their billing inquiries and issues.", model=llm_model)
refund_agent=Agent(name="Refund Agent", instructions="You are a refund agent. You can help customers with their refund inquiries and issues.", model=llm_model)

triage_Agent= Agent(
    name="Traige Agent",
    instructions="You are a triage agent. You can help customers with their inquiries and issues and route them to the appropriate agent.",
    model=llm_model,
    handoffs=[BillingAgent , handoff(refund_agent)]
)

async def main():
    result = await Runner.run(triage_Agent, "My card was charged twice.")
    print(result.final_output)
    print(result.last_agent)
    print(result.new_items)

asyncio.run(main())