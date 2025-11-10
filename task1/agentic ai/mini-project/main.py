import json
import requests
from agents import  function_tool

@function_tool
def fatch_user_data():
	""""Fetch function for user data and return list of users"""
	url = "https://jsonplaceholder.typicode.com/users"
	resp = requests.get(url)
	return resp.json()
	

print(fatch_user_data())    