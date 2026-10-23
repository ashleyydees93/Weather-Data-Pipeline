
import requests
import pandas as pd
from datetime import datetime, timezone

# Cities and their coordinates
cities = {
    "Wilmington": (34.2257, -77.9447),
    "Raleigh": (35.7796, -78.6382),
    "Charlotte": (35.2271, -80.8431),
    "Asheville": (35.5951, -82.5515)
}

url = "https://api.open-meteo.com/v1/forecast"
weather_data = []

# Collect weather data for each city
for city, (latitude, longitude) in cities.items():
    parameters = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph"
    }

    response = requests.get(url, params=parameters, timeout=15)
    response.raise_for_status()

    weather = response.json()["current"]

    weather_data.append({
        "city": city,
        "observation_time": weather["time"],
        "temperature_f": weather["temperature_2m"],
        "wind_speed_mph": weather["wind_speed_10m"]
    })

# Organize results into a table
df = pd.DataFrame(weather_data)

# Save data as a CSV file
df.to_csv("data/weather_data.csv", index=False)

print(df)
print("\nWeather data saved to data/weather_data.csv")
