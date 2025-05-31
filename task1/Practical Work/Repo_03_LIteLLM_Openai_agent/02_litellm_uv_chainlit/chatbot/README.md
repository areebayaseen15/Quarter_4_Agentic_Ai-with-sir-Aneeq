# 🤖 Gemini Chatbot with Chainlit & LiteLLM

This is a conversational chatbot built using **[Chainlit](https://docs.chainlit.io/)** and **[LiteLLM](https://docs.litellm.ai/)**. It integrates **Gemini** (Google’s LLM) to answer user questions in a chat interface.

---

## 🧠 Features

- ✅ Interactive chat interface via Chainlit
- ✅ LLM responses via Gemini (powered through LiteLLM)
- ✅ Stores chat history as a JSON file
- ✅ Uses `.env` file to secure your API key

---

## 🛠️ Tech Stack

- `Python`
- `Chainlit` – for real-time chat UI
- `LiteLLM` – to simplify interaction with Gemini API
- `python-dotenv` – for managing environment variables

---

## 📁 Project Structure
```
📦chatbot/
┣ 📄app.py
┣ 📄.env
┣ 📄chat_history.json
┣ 📄requirements.txt
┗ 📄README.md

```

---

## 🔧 Setup Instructions

### 1. Setting the project

```bash
uv init chatbot
cd chatbot
uv add chainlit python_dotenv litellm
uv .venv
.venv\Scripts\activate
```
2. Create a .env File
Make a .env file in the root directory and add your Gemini key:
```
GEMINI_API_KEY=your_gemini_api_key_here
```
🔐 Note: Use the Gemini key provided directly by Google or through your preferred provider, not OpenRouter.

3. Install Dependencies
Create a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```
Install required libraries:
```
pip install -r requirements.txt
```
4. Run the App
```
chainlit run app.py
```
Now open http://localhost:8000 in your browser to chat with the bot.

📤 Output
User queries and assistant responses are saved to chat_history.json automatically when the chat ends.

📦 requirements.txt
```
chainlit
litellm
python-dotenv
```
📌 Notes
Make sure your API key has access to Gemini's latest models.

You can change the model used inside app.py (e.g., gemini/gemini-1.5-flash or gemini/gemini-2.0-pro).

🙋‍♀️ Author
Areeba Yaseen
