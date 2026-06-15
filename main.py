import requests
import tkinter as tk
from tkinter import messagebox



# WEATHER API FUNCTION

def get_weather(city):

    API_KEY = "8ad393c37366f52f26beba7263b3ef2c"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    response = requests.get(url, timeout=10)
    data = response.json()

    forecast = data['weather'][0]['description']

    temp_k = data['main']['feels_like']
    temp_c = round(temp_k - 273.15, 1)

    return forecast, temp_c

# COUNTRY API 

def get_country_info(country):

    url = f"https://restcountries.com/v3.1/name/{country}"

    response = requests.get(url, timeout=10)
    data = response.json()[0]

    population = data['population']
    capital = data['capital'][0]
    region = data['region']

    currency_code = list(data['currencies'].keys())[0]

    return population, capital, region, currency_code


# EXCHANGE RATE FUNCTION

def get_exchange_rate(currency):

    url = f"https://open.er-api.com/v6/latest/{currency}"

    response = requests.get(url, timeout=10)
    data = response.json()

    usd_rate = data["rates"]["USD"]

    return usd_rate


# MAIN BUTTON FUNCTION

def search():

    city = city_entry.get()
    country = country_entry.get()

    try:

        forecast, temp = get_weather(city)

        population, capital, region, currency = get_country_info(country)

        usd_rate = get_exchange_rate(currency)

        results = f"Weather Forecast: {forecast}" \
f"\nTemperature: {temp}°C" \
f"\nCountry: {country}" \
f"\nCapital: {capital}" \
f"\nRegion: {region}" \
f"\nPopulation: {population:,}" \
f"\nCurrency: {currency}" \
f"\n1 {currency} = {usd_rate:.2f} USD"

        result_label.config(text=results)

    except Exception:
        messagebox.showerror(
            "Error",
            "Please enter a valid city and country."
        )

# GUI


window = tk.Tk()
window.title("Country Information Dashboard")
window.geometry("600x500")

title = tk.Label(
    window,
    text="Country Information Dashboard",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

country_label = tk.Label(window, text="Enter Country:")
country_label.pack()

country_entry = tk.Entry(window, width=30)
country_entry.pack()

city_label = tk.Label(window, text="Enter City:")
city_label.pack()

city_entry = tk.Entry(window, width=30)
city_entry.pack()

search_button = tk.Button(
    window,
    text="Get Information",
    command=search
)

search_button.pack(pady=10)

result_label = tk.Label(
    window,
    text="Results will appear here",
    justify="left",
    font=("Arial", 11)
)

result_label.pack(pady=20)

window.mainloop()



