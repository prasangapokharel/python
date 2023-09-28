
import requests

def get_weather_temperature(api_key, country, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": f"{city},{country}",
        "units": "metric",  # Use "imperial" for Fahrenheit
        "appid": api_key
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            temperature = data["main"]["temp"]
            return temperature
        else:
            print(f"Error: {data['message']}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    api_key = "59cc24e765e568ba2753b11ccbe83d4a"  # Replace with your API key
    country = "NP"  # Replace with the desired country code (e.g., "US" for United States)
    city = "Inaruwa"  # Replace with the desired city name

    temperature = get_weather_temperature(api_key, country, city)
    if temperature is not None:
        print(f"Temperature in {city}, {country}: {temperature}°C")
