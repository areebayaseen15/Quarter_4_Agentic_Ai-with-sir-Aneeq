# 🤖 AI CLI Chat with OpenRouter & LiteLLM

This is a simple Python CLI (Command Line Interface) tool that allows users to interact with multiple AI models using [OpenRouter](https://openrouter.ai/) via the [LiteLLM](https://github.com/BerriAI/litellm) library.

---

## 📚 Project Overview

This project enables users to:

1. Select an AI model (OpenAI GPT-4o, Gemini 1.5 Flash, or Mistral 7B Instruct)
2. Input a query
3. Get a response from the selected model — all using the terminal.

The purpose is to demonstrate how you can build a unified AI interface with minimal effort using **LiteLLM**, which simplifies integration with multiple LLM providers.

---

## 🧰 Technologies Used

- **Python**
- **LiteLLM** – unified interface to call any AI model
- **OpenRouter** – routing API to access multiple models
- **python-dotenv** – to securely load API keys from `.env` file

---

## 🔧 How It Works

1. User runs the Python script.
2. The CLI prompts the user to **select a model**.
3. After model selection, the user is prompted to **enter a question**.
4. The response from the selected model is displayed in the terminal.

---

## 🧠 Available Models

These models are free (or have a generous free tier) on [OpenRouter](https://openrouter.ai/):

| Model        | Identifier                                 | Provider      |
|--------------|--------------------------------------------|---------------|
| GPT-4o       | `openrouter/openai/gpt-4o`                 | OpenAI        |
| Gemini Flash | `gemini/gemini-1.5-flash`                  | Google        |
| Mistral      | `openrouter/mistralai/mistral-7b-instruct` | Mistral AI    |

---

## 🚀 LiteLLM Integration

Instead of manually creating HTTP requests to each provider, this project uses **LiteLLM** to:

- Call different models with one `completion()` function
- Easily switch between model providers
- Automatically handle API tokens, formats, and responses

### ✅ Sample Usage in Code:

```python
from litellm import completion

response = completion(
    model="openrouter/openai/gpt-4o",
    messages=[
        {"role": "user", "content": "What is the capital of Pakistan?"}
    ],
    max_tokens=200
)
```

This one function handles the complete request to OpenRouter with the selected model.

🔐 Setup Instructions
Install required libraries:

```
pip install litellm python-dotenv
```
Create a .env file in your project folder and add your API key:

```
OPENROUTER_API_KEY=your_openrouter_api_key_here
```
You can get your free API key from: https://openrouter.ai

📂 File Structure
```
├── main.py
├── .env
├── README.md
└── requirements.txt
📝 Example Interaction
```
Choose model (openai/gemini/mistral): openai
Enter your query: Who is the founder of Pakistan?
=> Muhammad Ali Jinnah is the founder of Pakistan.
📌 Notes
All models used are supported via OpenRouter.

LiteLLM makes switching between models seamless.

Ideal for learning how to work with LLM APIs efficiently.

💬 License
This project is open-source and free to use for educational and personal purposes.

🤝 Credits
Created by Areeba Yaseen using:

LiteLLM

OpenRouter
