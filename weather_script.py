import requests

def get_weather_data(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()

api_key = "your_api_key_here"
city = input("Enter the city: ")
weather_data = get_weather_data(city, api_key)

print(f"Weather in {city}:")
print(f"Temperature: {weather_data['main']['temp']} degree Celsius")
print(f"Humidity: {weather_data['main']['humidity']}%")
print(f"Description: {weather_data['weather'][0]['description']}")