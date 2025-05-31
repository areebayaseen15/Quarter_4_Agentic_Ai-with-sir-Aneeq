# Gemini API Assistant (Sync vs Async Demo)

This project demonstrates how to use the **Google Gemini API** using both **asynchronous** (`async`) and **synchronous** (`sync`) approaches with Python. The project uses an AI agent to respond to a simple prompt:  
> **"Tell me about recursion in programming."**

---

## 🔧 Features

- Loads environment variables using `.env`
- Connects to Gemini API using an OpenAI-compatible client
- Uses an `Agent` to process a prompt
- Supports **async** and **sync** versions for comparison

---

## 📁 File Structure
```
project/
│
├── agents/ # Contains Agent and Runner logic
├── .env # Environment file with API key
├── main_async.py # Asynchronous implementation
├── main_sync.py # Synchronous implementation
└── README.md # This file

```

---

## ✅ Requirements
```
- Python 3.8+
- `python-dotenv`
- Gemini-compatible OpenAI wrapper (like `AsyncOpenAI`, `OpenAIChatCompletionsModel`)
```
Install dependencies:

```bash
pip install -r requirements.txt
```
🌐 .env File
Create a .env file in your project root and add your Gemini API key:

```
GEMINI_API_KEY=your_google_gemini_api_key_here
```
🚀 How to Run
Asynchronous Version:
```
python main_async.py
Synchronous Version:
```
python main_sync.py
```
🔄 Sync vs Async – What's the Difference?
Feature	Sync	Async
Execution Style	Runs one task at a time	Can run multiple tasks concurrently
Performance	Slower if waiting on network/IO	Faster in network/IO heavy tasks
Use Case	Simple, blocking code	Ideal for API calls, real-time apps
Code Example	requests.get(url)	await aiohttp.get(url)
Python Tools	requests, http.client	aiohttp, asyncio

Why Use Async Here?
Calling an external API (Gemini) is a network-bound task. Using async allows your application to wait for the response without blocking other parts of your code — making it scalable and efficient.

🤖 Example Output
```
Function calls itself,
Looping in smaller pieces,
Endless by design.
```
📌 Summary
This project helps you understand:

How to interact with the Gemini API using an AI agent.

The difference between synchronous and asynchronous Python code.

Why asynchronous programming is more efficient for I/O-bound tasks like API calls.

