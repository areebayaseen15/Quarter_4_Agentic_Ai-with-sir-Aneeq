
from agents import Agent , Runner , OpenAIChatCompletionsModel , AsyncOpenAI , RunConfig

gemini_client = AsyncOpenAI(
    api_key="AIzaSyCBZy5su0PPRwQhWCPdH_wryU7mJr50gV8",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
#################################3Agent level Configuration############
# Yahan model agent banate waqt hi set ho gaya
agent = Agent(
    name= "Patriotic Poetry Bot",
    instructions="You are a patriotic agent , you will say patriotic poetry in Urdu for our beloved country Pakistan, Whenever you are querry regarding Pakistan.",
    model=OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=gemini_client,
    )
)

# Run karna normal tarike se
result = Runner.run_sync(agent, "Describe the Pakistan.")
print(result.final_output)


# run level confuguration

gemini_client = AsyncOpenAI(
    api_key="AIzaSyCBZy5su0PPRwQhWCPdH_wryU7mJr50gV8",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model=OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=gemini_client,
    )

config = RunConfig(
    model=model,
    model_provider=gemini_client
)

agent= Agent(
    name="Areeba's Assistant",
    instructions="You are helpful assitant of Areeba."

)

result = Runner.run_sync(agent, "Describe the Pakistan." ,run_config=config)
print(result.final_output)



################################3Global Level
from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client

# Gemini ka client
gemini_client = AsyncOpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Global level pe set kar diya
set_default_openai_client(gemini_client)

# Ab koi bhi agent default se Gemini use karega
agent = Agent(name="AnyBot", instructions="You are friendly.", model="gemini-2.0-flash")

result = Runner.run_sync(agent, "Tell me a joke.")
print(result.final_output)
