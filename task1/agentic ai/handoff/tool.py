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


# tool calling
class Location(TypedDict):
    lat: float
    long: float

# function tool override
@function_tool(
        name_override="Fetch_Weather",  #no space give undersore in name
        description_override="Fetch weather for a given description"
)  
async def fetch_weather(location: str) -> str:
    # docstring
    """Fetch the weather for a given location.

        Args:
        location: The location to fetch the weather for.
    """
    return "sunny"

@function_tool
async def get_sum(a:int , b:int):
    return a+b
agent = Agent(
    name="Helpful agent",
    instructions="You are a helpful agent that help users with their querries.",
    model=model,
    tools=[fetch_weather , get_sum],
    # tool_use_behavior="run_llm_again"
    tool_use_behavior="stop_on_first_tool"
)
# print("Registered Tools:")
# for tool in agent.tools:
#     print("-", tool.name, "| Description:", tool.description)


query = input("Type your query: ")
result = Runner.run_sync(
        agent,
        query,
        run_config=config,
    )
print("tools" , agent.tool)
print(result.final_output)

# ttolrition schema call invoke tool
# decorater ma kuch feature hoay hain jo wrape kr detay hain
# tool ki description agents docstring sa laiga
#jb tool caling krwatay hain to llm k pass as a schema jata ha llm direct ni smjh pata
#llm ka pass jb schema bn k jata ha to ismay jata ha tool ka anme , uski properties means kon konsay
# parameter required hain and tool ki desciption



# context 2 trhan k hotay hain ek local and ek jo llm kl pass jata ha
# sdk ma chahaya tool syncronous ho ya asyncronus dono tool ko kr laiga 



# prhna ha tool use behaiour
# Asyncio library 

# streaming chunk by chunk data provide hota ha


#
