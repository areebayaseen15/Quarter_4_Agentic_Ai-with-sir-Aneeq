import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
import asyncio


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")


external_client = AsyncOpenAI(
    api_key=api_key,
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



async def main():
    agent = Agent(
       name="HelloAgent",
       instructions= "You are a helpful assistant that greets users.",
       model =model,
   )
    
    
    result = await Runner.run(agent, input("Enter your querry: "), run_config=config)
    print(result.final_output)
    
    

if __name__ == "__main__":
    asyncio.run(main())        