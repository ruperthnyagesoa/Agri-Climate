import requests
import json


def get_temperature_forecast(forecast_days, latitude, longitude):
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,precipitation_probability&forecast_days={forecast_days}"
# Send the API request
    response = requests.get(api_url)