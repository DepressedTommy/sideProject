import requests
from datetime import datetime

# -*- coding: utf-8 -*-

api_key = 'ac0dcccca4c4872d8ddc59c577a4f70a'

def get_current_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # You can change the units to metric or imperial as per your preference
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)

        weather_data = response.json()
        return weather_data

    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        return None
    
def get_pt_data():
    cities = ["Lisbon", "Porto" , "Vila Nova de Gaia" , "Amadora" , "Braga", "Setubal" ,"Coimbra", "Faro", "Azores", "Madeira"]

    all_city_data = []
    for city in cities:
        weather_data = get_current_weather(city, api_key)
        if weather_data:
            city_info = {
                "city": city,
                "temperature": weather_data['main']['temp'],
                "humidity": weather_data['main']['humidity'],
                "weather_description": weather_data['weather'][0]['description'],
                "sunset_time": datetime.utcfromtimestamp(weather_data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')
            }
            all_city_data.append(city_info)
    
    return all_city_data
    
    
city_name = 'Porto'  # Replace with the desired city name
country_code = 'PT'