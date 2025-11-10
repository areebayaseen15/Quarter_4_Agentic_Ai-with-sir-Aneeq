import asyncio
from agents import Agent , Runner , OpenAIChatCompletionsModel , AsyncOpenAI, handoff , set_tracing_disabled
import os

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


fitness_coach = Agent(
    name = "Fitness Coach",
    instructions= "You're a running coach. Ask 1-2 quick questions, then give a week plan. "
        "Keep it simple and encouraging. No medical advice.",
    model=llm_model
)

study_coach = Agent(
    name="Study Coach",
    instructions=(
        "You're a study planner. Ask for current routine, then give a 1-week schedule. "
        "Keep steps small and doable."
    ),
)

router = Agent(
    name="Coach Router",
    instructions=(
        "Route the user:\n"
        "- If message is about running, workout, stamina → handoff to Fitness Coach.\n"
        "- If it's about exams, study plan, focus, notes → handoff to Study Coach.\n"
        "After handoff, the specialist should continue the conversation."
    ),
    handoffs=[study_coach, handoff(fitness_coach)],
    model=llm_model
)

async def main():
    result1 = await Runner.run(router , "I want to improve my running stamina")
    print(result1.final_output)
    

    specialist = result1.last_agent

# second turn with the same coach
    result2 = result1.to_input_list() + [
        {"role" : "user" , "content" : "Nice. What should I eat on training days? "}
    ]
    t2_input = await Runner.run(specialist, result2)
    print("\nTurn 2 (specialist reply):\n", t2_input.final_output)

# 3rd turn
    result3 = result2.to_input_list() + [
        {"role" : "user" , "content" : "What about on rest days?"}
    ]
    t3_input = await Runner.run(specialist, result3)
    print("\nTurn 3 (specialist reply):\n", t3_input.final_output)
