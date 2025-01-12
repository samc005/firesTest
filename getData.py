from bs4 import BeautifulSoup
import requests
import geocoder

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
    api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=84966bc0183e5a020a9110359cc70409&units=metric" 
    response = requests.get(api_url)
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

