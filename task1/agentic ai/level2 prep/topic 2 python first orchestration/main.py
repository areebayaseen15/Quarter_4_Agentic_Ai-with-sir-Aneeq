from agents import Agent, FunctionToolResult , Runner , FunctionTool , RunContextWrapper
from typing import Any , List
from agents.agent import ToolsToFinalOutputResult

@FunctionTool
def get_weather(city:str)->str:
    """Get the weather of a city."""
    return f"The weather in {city} is sunny."



def custom_tool_handler(ctx:RunContextWrapper[Any] , tool_results:List[FunctionToolResult])->ToolsToFinalOutputResult:
    # Custom logic to process tool results and generate final output
    for result in tool_results:
        if result.output and "Sunny" in result.output:
            return ToolsToFinalOutputResult(
                is_final_output=True,
                final_output=f"Final result: {result.output}"
            )
        return ToolsToFinalOutputResult(
            is_final_output=False,
            final_output=None

        )
    
agent = Agent(
    name="Weather Agent",
    instructions="Retrieve weather details.",
    tools=[get_weather],
    tool_use_behavior=custom_tool_handler
)    

