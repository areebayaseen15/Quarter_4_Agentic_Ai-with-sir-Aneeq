import requests , pprint

url = "https://api.open-meteo.com/v1/forecast?latitude=51.5&longitude=-0.12&current_weather=true"
response = requests.get(url , timeout=10)
response.raise_for_status()
weather = response.json()
pprint.pp(weather)


url = "https://catfact.ninja/fact"
resp = requests.get(url, timeout=10)
resp.raise_for_status()
print(resp.json()['fact'])
     

# open api key     

import os, openai

# 🔑 TODO: Replace with your own key or set OPENAI_API_KEY in the environment
openai.api_key = OPENAI_API_KEY

response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say hello! I'm Wania"}]
)
print(response.choices[0].message.content)



response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "What's my name?"}]
)
print(response.choices[0].message.content)