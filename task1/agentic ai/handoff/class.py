import asyncio
from typing import TypedDict
from agents import Agent, OpenAIChatCompletionsModel, RunConfig, Runner, function_tool
from openai import AsyncOpenAI
import os
# from dotenv import load_dotenv

# load_dotenv()

# Note: This is not an actual OpenAI API key; seems like you are trying to use Google Gemini
google_api_key = "AIzaSyC7JtvQM1BJCl36Tix55p8e4r95Hc2CSOk"  

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


agent = Agent(
    name="StructuredWeatherAgent",
    instructions="Use the final_output tool with WeatherAnswer schema.",
    # output_type=WeatherAnswer,
    # tools=[fetch_weather]
    
)



#on invoke tool ek property ha jis may hmny function pass kia wo ha