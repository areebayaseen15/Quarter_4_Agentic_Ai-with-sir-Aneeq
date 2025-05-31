# main.py
import os
from dotenv import load_dotenv
import chainlit as cl
from litellm import completion
import json

# Load API key
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("API key not found in .env")

# Initialize Chainlit
@cl.on_chat_start
async def start():
    cl.user_session.set("chat_history", [])
    await cl.Message(content="Welcome to the AI Assistant! How can I help you?").send()

# Handle incoming messages
@cl.on_message
async def main(message: cl.Message):
    msg = cl.Message(content="Thinking...")
    await msg.send()

    history = cl.user_session.get("chat_history") or []
    history.append({"role": "user", "content": message.content})

    try:
        response = completion(
            model="gemini/gemini-2.0-flash",
            api_key=gemini_api_key,
            messages=history
        )
        reply = response.choices[0].message.content
        msg.content = reply
        await msg.update()

        history.append({"role": "assistant", "content": reply})
        cl.user_session.set("chat_history", history)

    except Exception as e:
        msg.content = f"Error: {str(e)}"
        await msg.update()

@cl.on_chat_end
async def on_chat_end():
    history = cl.user_session.get("chat_history") or []
    with open("chat_history.json", "w") as f:
        json.dump(history, f, indent=2)
