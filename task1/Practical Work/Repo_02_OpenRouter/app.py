import streamlit as st  # type: ignore
import asyncio
from dotenv import load_dotenv  # type: ignore
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled  # type: ignore
import os

# Load environment variables
load_dotenv()
set_tracing_disabled(True)

# Inject custom CSS styles
st.markdown("""
    <style>
        body {
            background-color: #f7f9fc;
        }

        .title {
            font-size: 32px;
            font-weight: 700;
            color: #FF4B4B;
            margin-bottom: 20px;
        }

        .chat-container {
            display: flex;
            possition: relative;
            flex-direction: column;
            gap: 10px;
            margin-bottom: 20px;
        }

        .message-row {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            width: 100%;
        }

        .message.user {
            background-color: #e3f2fd;
            color: #0d47a1;
            align-self: flex-start;
            border-radius: 18px 18px 18px 0;
        }

        .message.assistant {
            background-color: #fff9c4;
            color: #795548;
            align-self: flex-end;
            border-radius: 18px 18px 0 18px;
        }

        .message {
            max-width: 75%;
            padding: 14px 18px;
            font-size: 15px;
            line-height: 1.5;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .stButton>button {
            border-radius: 8px;
            background-color: #FF4B4B;
            color: white;
            font-weight: 600;
        }

        .stButton>button:hover {
            background-color: #ff7777;
        }

        .chat-input input {
            border-radius: 10px;
            padding: 10px;
            position: fixed;
        }

        .sidebar .sidebar-content {
            background-color: #f0f2f6;
        }
    </style>
""", unsafe_allow_html=True)

# Model options
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

# Sidebar
st.sidebar.title("⚙️ Settings")
selected_model_label = st.sidebar.selectbox("🧠 Select Model", options=list(MODEL_OPTIONS.keys()))
# Add New Chat button in sidebar
if st.sidebar.button("🆕 New Chat"):
    st.session_state.chat_history = []


# Title
st.markdown('<div class="title">🤖 AI Agent with Model Selection</div>', unsafe_allow_html=True)

# Session state initialization
if "current_model" not in st.session_state or st.session_state.current_model != selected_model_label:
    st.session_state.current_model = selected_model_label
    st.session_state.chat_history = []
    st.session_state.agent = create_agent(MODEL_OPTIONS[selected_model_label])

agent = st.session_state.agent

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat display
def display_chat():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for chat in st.session_state.chat_history:
        role_class = "user" if chat["role"] == "user" else "assistant"
        align_class = "justify-content-start" if chat["role"] == "user" else "justify-content-end"
        st.markdown(
            f'<div class="message-row {align_class}"><div class="message {role_class}">{chat["content"]}</div></div>',
            unsafe_allow_html=True
        )
    st.markdown('</div>', unsafe_allow_html=True)

# Chat input form
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("💬 Your message:", key="chat_input")
    submitted = st.form_submit_button(" Send")

# Process user input
if submitted and user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    with st.spinner("Assistant is typing... 💬"):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        conversation_text = ""
        for chat in st.session_state.chat_history:
            prefix = "User: " if chat["role"] == "user" else "Assistant: "
            conversation_text += prefix + chat["content"] + "\n"

        response = loop.run_until_complete(Runner.run(agent, conversation_text))
        assistant_message = response.final_output.strip()

    st.session_state.chat_history.append({"role": "assistant", "content": assistant_message})

# Show chat
display_chat()
