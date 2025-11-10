# Example: Exploring Runner.run() result

from openai import OpenAI
from openai.agents import Agent, Runner

# 1️⃣ Create a simple agent
echo_agent = Agent(
    name="EchoAgent",
    instructions="Repeat exactly what the user says."
)

# 2️⃣ Make a runner
runner = Runner(client=OpenAI())

# 3️⃣ Run the agent
result = runner.run(
    agent=echo_agent,
    input="Hello Areeba!"
)

# 4️⃣ Explore result properties
print("💬 Final Output:", result.final_output)
print("🤖 Last Agent:", result.last_agent.name)
print("📦 New Items:", [item.type for item in result.new_items])
print("🔁 Input List:", result.to_input_list())
print("🛡️ Input Guardrails:", result.input_guardrail_results)
print("🛡️ Output Guardrails:", result.output_guardrail_results)
print("📨 Raw Responses:", result.raw_responses)
print("🪪 Original Input:", result.input)
