
from ast import main
import asyncio
from agents import Agent, RunConfig , Runner , OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from openai.types.responses import ResponseTextDeltaEvent
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = "AIzaSyC7JtvQM1BJCl36Tix55p8e4r95Hc2CSOk"

async def main():
    external_client = AsyncOpenAI(
        api_key=gemini_api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

    model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=external_client
    )
    config = RunConfig(
        model=model,
        model_provider=external_client,
        tracing_disabled=True
    )

    agent = Agent(
        name="My Streaming Agent",
        instructions="You are a helpful assistant that streams responses.",
        model="gemini-1.5-pro"
    )

    result = Runner.run_streamed(
        agent,
        input="Tell me the current news about Summud Flotilla which were sailing to Gaza?",
        run_config=config
    )
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
