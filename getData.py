from bs4 import BeautifulSoup
import requests
import geocoder
import pandas as pd
import math

def get_weather_data(latitude, longitude):
  """
  Fetches weather data (wind, humidity, temperature, precipitation) 
  from a specific weather API using latitude and longitude.

  Args:
    latitude: Latitude coordinate.
    longitude: Longitude coordinate.

  Returns:
    A dictionary containing the scraped data.
  """

  try:
    # Replace with your preferred weather API endpoint
    api_weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=84966bc0183e5a020a9110359cc70409&units=metric" 
    response = requests.get(api_weather_url)
    response.raise_for_status()  # Raise an exception for bad status codes

    data = response.json()

    # Extract weather data from the API response
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']*3.6
    precipitation = data.get('rain', {}).get('1h', 0)  # Check for precipitation data (may vary by API)

    return {
        "temperature": temperature,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "precipitation": precipitation
    }

  except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    return None
  except KeyError as e:
    print(f"Error parsing API response: {e}")
    return None


def get_fire_data (latitude, longitude):
  try:
  # FIRMS API URL to get active fire data (you may need to provide an API key)
    df_fire = pd.read_csv('df_fire.csv')

    # Haversine function to calculate the distance between two lat/lon points
    def haversine(lat1, lon1, lat2, lon2):
        R = 6371  # Radius of Earth in kilometers
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)

        dlat = lat2_rad - lat1_rad
        dlon = lon2_rad - lon1_rad

        a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = R * c
        return distance

    # Calculate the distance from each fire to your location
    df_fire['distance'] = df_fire.apply(lambda row: haversine(latitude, longitude, row['latitude'], row['longitude']), axis=1)

    # Sort the DataFrame by the 'distance' column (ascending order)
    df_fire_sorted = df_fire.sort_values(by='distance', ascending=True)

    # The nearest fire will now be the first row
    nearest_fire = df_fire_sorted.iloc[0]

    return {
        "fire_latitude": nearest_fire['latitude'],
        "fire_longitude": nearest_fire['longitude'],
        "distance": nearest_fire['distance'],
    }

  except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    return None
  except KeyError as e:
    print(f"Error parsing API response: {e}")
    return None

