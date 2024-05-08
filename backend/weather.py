import requests
import json


def get_temperature_forecast(forecast_days, latitude, longitude):
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,precipitation_probability&forecast_days={forecast_days}"
    # Send the API request
    response = requests.get(api_url)
    # Process the response
    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=2))
        if "hourly" in data and "temperature_2m" in data["hourly"]:
            temperature_data = data["hourly"]["temperature_2m"]
            preceipitation_data = data["hourly"]["precipitation_probability"]
            # Extract the temperature forecast for the last date
            last_date_temperatures = temperature_data[-12:]
            temperature = last_date_temperatures[-1]
            last_precipitation_data = preceipitation_data[-12:]
            preceipitation = last_precipitation_data[-1]
            return temperature, preceipitation
        else:
            return None
    else:
        print("API request failed with status code:", response.status_code)
        return None


def geocode_location(address="13024 Green Valley Rd, Sebastopol, CA 95472"):
    api_url = "http://api.positionstack.com/v1/forward"
    access_key = "1db69d9dca8eec0e7f916c78f7bc0f65"