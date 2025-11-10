from agents import Agent , Runner , AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled , function_tool
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
set_tracing_disabled(disabled=True)

external_Client = AsyncOpenAI(
    api_key=os.getenv("gemini_key"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_Client
)

@function_tool
def calculate(a:int , b:int , operation:str="add"):
    """use this tool instead of guessing calculations yourself"""

    operation = operation.lower()
    if not isinstance(a , int) or not isinstance(b , int):
        return "Invalid input. Please provide two integers."
    
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return f"Invalid operation '{operation}'. Please use add, subtract, multiply, or divide."


math_agent = Agent(
    name="Math Agent",
    instructions="You are a math expert agent.Always use the calculate tool for solving math operations",
    tools=[calculate],
    model=model
)
response = Runner.run_sync(math_agent , "Add 5 and 3 equals to what?")
print(response.final_output)

response = Runner.run_sync(math_agent , "Add 5 and 3 to what?.And tell me which tool you used to get the answer")
print(response.final_output)

response = Runner.run_sync(math_agent , "Divide five and zero equals to what?.And tell me which tool you used to get the answer")
print(response.final_output)

response = Runner.run_sync(math_agent , "Divide five and zero equals to what?.And tell me which tool you used to get the answer")
print(response.final_output)