# 🌤️ Gemini Weather Assistant (Haiku Style)

This Python project demonstrates how to build a simple AI agent using the `agents` library and Google's Gemini model (`gemini-2.0-flash`). The agent responds to questions in **haiku format** and can answer questions like the weather in a given city.

---

## 📦 Features

- Uses **Google Gemini 2.0 Flash** model via `LiteLLM`.
- Responds only in **haikus** (as per instructions).
- Supports **tool calling**: includes a `get_weather()` function tool.
- Runs asynchronously using Python's `asyncio`.

---

## 🧰 Requirements

Install the following Python packages:

```bash
pip install agents litellm python-dotenv

```
⚠️ Note: You must be using Python 3.10 or above.

🔐 Environment Setup
Create a .env file in your project directory and add your Gemini API key:

```
GEMINI_API_KEY=your_actual_api_key_here
```
🚀 How to Run
Make sure your .env file is created and contains your API key.

Run the script:
```
python your_script_name.py
```
If you're using Google Colab:

```
# First, upload your .env file to the session.
from google.colab import files
files.upload()
```
# Then run the script as shown.
🔧 Function Tool

The function get_weather(city: str) is exposed to the agent and can be invoked as a tool when the prompt requires it.

Example:
```
@function_tool
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny."

    ```
📤 Sample Output
When you ask:
```
What's the weather in Tokyo?
You’ll receive something like:
Sky above Tokyo,  
Warm sun kisses cherry trees,  
Peaceful breeze whispers.
```

📚 Dependencies
agents

litellm

python-dotenv

asyncio (standard library)

os (standard library)

❗ Troubleshooting
Event Loop Already Running (in Colab)
If you get an error like:

```

RuntimeError: This event loop is already running
```

Use:

```

await main(model=MODEL, api_key=GEMINI_API_KEY)
instead of asyncio.run(...) in Google Colab.
```

👤 Author
Developed by Areeba Yaseen