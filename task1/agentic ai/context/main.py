import json
from typing import List, Optional, Dict
from agents import Agent, OpenAIChatCompletionsModel, RunConfig, Runner, RunContextWrapper, function_tool
from openai import AsyncOpenAI
from pydantic import BaseModel
import asyncio

gemini_api_key = "AIzaSyC7JtvQM1BJCl36Tix55p8e4r95Hc2CSOk"

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

class UserSessionsContext(BaseModel):
    name: str
    uid: int
    goal: Optional[dict] = None
    diet_preferences: Optional[str] = None
    workout_plan: Optional[dict] = None
    meal_plan: Optional[List[str]] = None
    injury_notes: Optional[str] = None
    handoff_logs: List[str] = []
    progress_logs: List[Dict[str, str]] = []

@function_tool()
async def get_user_sessions_context(context: RunContextWrapper[UserSessionsContext]) -> UserSessionsContext:
    print("Tool executed: get_user_sessions_context")
    return context.context


async def main():
    user_context = UserSessionsContext(
        name="John Doe",
        uid=123,
        goal={"type": "weight_loss", "target": 70},
        diet_preferences="vegetarian",
        workout_plan={"type": "strength", "duration": "30min"},
        meal_plan=["salad", "smoothie", "grilled vegetables"],
        injury_notes="None"
    )

    # context_wrapper = RunContextWrapper(context=user_context)

    agent = Agent[UserSessionsContext](
        name="Assistant",
        instructions=(
            "You are a helpful fitness assistant. "
            "Use the provided tool to retrieve the user's context information, including name, goal, diet preferences, "
            "workout and meal plans."
        ),
        tools=[get_user_sessions_context],
        
        # output_type=UserSessionsContext
        
    )

    result = await Runner.run(
        starting_agent=agent,
        input="Use the available tool to retrieve the user's name, goal, diet preference, workout plan, and meal plan.",
        context =user_context,
        run_config=config
    )

    print(result.final_output)

asyncio.run(main())
