from __future__ import annotations

import asyncio

from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
set_tracing_disabled(disabled=True)
from dotenv import load_dotenv

load_dotenv()

MODEL = 'gemini/gemini-2.0-flash'
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY is None:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")



@function_tool
def get_weather(city: str)->str:
    print(f"[debug] getting weather for {city}")
    return f"The weather in {city} is sunny."


async def main(model: str, api_key: str):
  agent = Agent(
      name="Assistant",
      instructions="You only respond in haikus.",
      model=LitellmModel(model=model, api_key=api_key),

  )
  result = await Runner.run(agent, "What's the weather in Tokyo?")
  print(result.final_output)


asyncio.run(main(model=MODEL, api_key=GEMINI_API_KEY))

