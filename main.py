import requests
import tkinter as tk
from tkinter import messagebox



# WEATHER API FUNCTION

def get_weather(city):

    API_KEY = "My api key for weather"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    response = requests.get(url, timeout=10)
    data = response.json()

    forecast = data['weather'][0]['description']

    temp_k = data['main']['feels_like']
    temp_c = round(temp_k - 273.15, 1)

    return forecast, temp_c



