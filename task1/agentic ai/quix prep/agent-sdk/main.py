
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
import asyncio
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

math_Agrnt :Agent = Agent(
    name="Math_AGent",
    instructions="You are a math expert. You can solve complex math problems step by step.",
    model=llm_model,
)

# syncronouly
result = Runner.run_sync(math_Agrnt , "What is the benefit of using math agents?")

print("Result: ", result)


# Asynchronously
async def main():

    result: Runner = await Runner.run(math_Agrnt, "Tell me about recursion in programming.")

    print(result.final_output)


asyncio.run(main())
     