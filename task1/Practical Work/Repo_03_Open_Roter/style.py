import streamlit as st # type: ignore
import asyncio
from dotenv import load_dotenv # type: ignore
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled # type: ignore
import os

load_dotenv()
set_tracing_disabled(True)

MODEL_OPTIONS = {
    "openai/gpt-3.5-turbo-16k": "openai/gpt-3.5-turbo-16k",
    "Mistral 7B Instruct": "mistralai/mistral-7b-instruct",
    "GPT-4o Mini (OpenAI)": "openai/gpt-4o-mini",
    "GPT-3.5 Turbo (OpenAI)": "openai/gpt-3.5-turbo",
}

@st.cache_resource(show_spinner=False)
def create_agent(model_name):
    provider = AsyncOpenAI(
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1/"
    )
    model = OpenAIChatCompletionsModel(
        model=model_name,
        openai_client=provider,
    )
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
        model=model
    )
    return agent

st.title("AI Agent with Model Selection")

selected_model_label = st.selectbox("Select Model", options=list(MODEL_OPTIONS.keys()))

if "current_model" not in st.session_state or st.session_state.current_model != selected_model_label:
    st.session_state.current_model = selected_model_label
    st.session_state.chat_history = []
    st.session_state.agent = create_agent(MODEL_OPTIONS[selected_model_label])

agent = st.session_state.agent

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def display_chat():
    for chat in st.session_state.chat_history:
        if chat["role"] == "user":
            st.markdown(f"**You:** {chat['content']}")
        else:
            st.markdown(f"**Assistant:** {chat['content']}")

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Your message:")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    with st.spinner("Assistant is typing..."):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        conversation_text = ""
        for chat in st.session_state.chat_history:
            prefix = "User: " if chat["role"] == "user" else "Assistant: "
            conversation_text += prefix + chat["content"] + "\n"

        response = loop.run_until_complete(
            Runner.run(agent, conversation_text)
        )
        assistant_message = response.final_output.strip()

    st.session_state.chat_history.append({"role": "assistant", "content": assistant_message})

display_chat()
