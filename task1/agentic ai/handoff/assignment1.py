import asyncio
from typing import TypedDict
from agents import Agent, OpenAIChatCompletionsModel, RunConfig, Runner, function_tool
from openai import AsyncOpenAI
import os
# from dotenv import load_dotenv

# load_dotenv()

# Note: This is not an actual OpenAI API key; seems like you are trying to use Google Gemini
google_api_key = "AIzaSyC7JtvQM1BJCl36Tix55p8e4r95Hc2CSOk"  # Safer

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


#tool 1
@function_tool
async def greet_user(name: str) -> str:
    """Greets the user with their name."""
    return f"Hello {name}, hope you're excited for your trip! ✈️"

#tool 2
@function_tool
async def suggest_top_places(city: str) -> list[str]:
    """Suggests top 3 places to visit in the given city."""
    suggestions = {
        "murree": ["Mall Road", "Patriata Chair Lift", "Pindi Point"],
        "lahore": ["Badshahi Mosque", "Lahore Fort", "Shalimar Gardens"],
        "islamabad": ["Faisal Mosque", "Daman-e-Koh", "Pakistan Monument"]
    }
    return suggestions.get(city.lower(), ["City guide not available"])

# tool 3
@function_tool
async def get_travel_essentials(weather: str) -> list[str]:
    """Returns a list of travel essentials based on weather condition."""
    if "cold" in weather.lower():
        return ["Warm Jacket", "Gloves", "Thermal Wear"]
    elif "hot" in weather.lower():
        return ["Sunscreen", "Water Bottle", "Cap"]
    else:
        return ["Umbrella", "Light Jacket", "Snacks"]

agent = Agent(
    name="Travel Planning Assistant",
    instructions="You help users prepare for their trip by converting currency, suggesting places to visit, and listing travel essentials based on weather.",
    model=model,
    tools=[greet_user, suggest_top_places, get_travel_essentials],
)


query = "My name is Areeba. I'm planning to visit Murree and the weather will be cold. Can you greet me, suggest places to visit, and tell me what I should pack?"
result = Runner.run_sync(
        agent,
        query,
        run_config=config,
    )
print(result.final_output)
