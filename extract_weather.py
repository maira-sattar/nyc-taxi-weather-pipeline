import requests
import pandas as pd

# Open-Meteo historical weather API for NYC (Central Park coordinates)
url = "https://archive-api.open-meteo.com/v1/archive"

params = {
    "latitude": 40.7128,
    "longitude": -74.0060,
    "start_date": "2023-12-31",   # match your taxi data's date range
    "end_date": "2024-01-31",
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,snowfall_sum",
    "timezone": "America/New_York"
}

response = requests.get(url, params=params)
print("Status code:", response.status_code)

data = response.json()

# The daily data comes as parallel arrays - convert to a clean DataFrame
weather_df = pd.DataFrame(data["daily"])
print(weather_df.head())
print("Shape:", weather_df.shape)

weather_df.to_csv("weather_sample.csv", index=False)
print("Saved to weather_sample.csv")