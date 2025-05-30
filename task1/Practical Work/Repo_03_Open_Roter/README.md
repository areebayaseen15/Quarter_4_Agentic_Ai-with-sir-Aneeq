# 🤖 AI Agent with Model Selection (Powered by OpenRouter)

This project is an interactive AI agent built with **Streamlit**, allowing users to dynamically select and chat with different large language models (LLMs) via the [OpenRouter](https://openrouter.ai/) API.

---

## 🌐 What is OpenRouter?

**OpenRouter** is a unified gateway to 50+ LLMs (Large Language Models), including both **free** and **paid** models like:

- OpenAI (GPT-4, GPT-3.5),
- Mistral,
- Claude,
- Google Gemini (with caveats),
- Meta’s LLaMA,
- and many more.

### ✅ Benefits of OpenRouter:

- **Single API Key** for all models.
- **Unified endpoint** (`/v1/chat/completions`) – no need to change core code for most models.
- **Fast switching** between models by just changing the `model` name and `base_url`.

### ⚠️ Note about Gemini and Others:
Some models like **Google Gemini** may **not fully follow** the OpenAI-style `chat/completions` format. For those models:
- Prompt format might differ (`prompt` vs `messages[]`).
- You may need **custom logic** if strict compatibility is needed.

---

## 🧠 Project Overview

This app is a **Streamlit-based AI chat agent** with a beautiful UI and built-in **model switching**. You can:

- Select from multiple models like GPT-4o, GPT-3.5, Mistral.
- Send messages and receive replies.
- Clear chat history with a "New Chat" button.
- See chat-style bubbles for user and assistant messages.

### 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [OpenRouter API](https://openrouter.ai/docs)
- [Python (AsyncIO)](https://docs.python.org/3/library/asyncio.html)
- `dotenv` for environment management

---

## 🚀 How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Quarter_4_Agentic_Ai-with-sir-Aneeq/task1/Practical Work/Repo_03_Open_Roter

   cd ai-agent-openrouter
```
---
Install dependencies:

```
pip install -r requirements.txt
```
---
Set your OpenRouter API Key in a .env file:

```
OPENROUTER_API_KEY=your_api_key_here
```
---
Run the app:

```
streamlit run app.py
```
---
🧪 Supported Models (Default)
You can easily customize this list in MODEL_OPTIONS:
----

```
MODEL_OPTIONS = {
    "openai/gpt-3.5-turbo-16k": "openai/gpt-3.5-turbo-16k",
    "Mistral 7B Instruct": "mistralai/mistral-7b-instruct",
    "GPT-4o Mini (OpenAI)": "openai/gpt-4o-mini",
    "GPT-3.5 Turbo (OpenAI)": "openai/gpt-3.5-turbo",
}
```

---
To add more models (like Claude or Gemini), update this dictionary and adjust prompt formatting if needed.

---
🧠 Agent Architecture
The agent uses the agent and Runner abstraction pattern:

Agent: Represents the AI model with system instructions.

Runner: Handles full conversation flow using message history and returns final outputs.

AsyncOpenAI: OpenRouter-compatible client to send requests asynchronously.

---
💡 Key Features
✅ Model Switching with Dropdown

✅ Clean and Styled Chat UI

✅ Streamlit Form and Event Handling

✅ Unified API Integration with OpenRouter


👩‍💻 Developed By
Areeba Yaseen


