

# structured output

import asyncio
from typing import TypedDict
from agents import Agent, OpenAIChatCompletionsModel, RunConfig, Runner, function_tool
from openai import AsyncOpenAI
import os
from pydantic import BaseModel


google_api_key = "" 


client = AsyncOpenAI(
    api_key=google_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    openai_client=client,
    model="gemini-2.5-flash",
)

config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)


class WeatherAnswer(BaseModel):
  location: str
  temperature_c: float
  summary: str
     


# Weather_obj = WeatherRequest(city="karachi" , weather="rainy" , temp="27C")

# @function_tool(
#         name_override="Fetch_Weather",  # no space, use underscore in name
#         description_override="Fetch weather for a given description"
# )
# def fetch_weather(location: str) -> WeatherAnswer:
#     return WeatherAnswer(location=location, temperature_c=27.0, summary="Rainy")

agent = Agent(
    name="StructuredWeatherAgent",
    instructions="Use the final_output tool with WeatherAnswer schema.",
    output_type=WeatherAnswer,
    # tools=[fetch_weather]
    
)


query = input("Type your query: ")
result = Runner.run_sync(
        agent,
        query,
        run_config=config,
        
    )
print(result.final_output)




#by default output string hota ha agr lkn kisi structure ma output lain to structured output
