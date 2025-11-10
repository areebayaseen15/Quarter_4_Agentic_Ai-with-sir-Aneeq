from agents import Agent , Runner , AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
import asyncio

set_tracing_disabled(disabled=True)

external_client : AsyncOpenAI = AsyncOpenAI(
    api_key="AIzaSyAjPhwuXX3q2jHv8Bg7SBO8btUWteYYW6o",

    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model :OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

recepie_bot : Agent = Agent(
    name="Receipie_Bot",
    instructions="You are a receipie bot , You can provide receipies based on the ingredients provided by the user.",
    model=model
)

async def main():

    result: Runner = await Runner.run(recepie_bot, "I have chicken , rice and tomatoes. What can I make for dinner?")

    print(result.final_output)


asyncio.run(main())