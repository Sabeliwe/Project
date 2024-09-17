import requests

# Replace with your actual OpenWeather API key
API_KEY = '6a5aa476acd6558fc60638511c222b55'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather_data(city):
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        
        # Check if response content is empty
        if not response.text.strip():
            raise ValueError("Empty response received from the API")
        
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as val_err:
        print(f"Value error occurred: {val_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

    return None  # Return None if an error occurred

# Example usage:
if __name__ == "__main__":
    weather_data = get_weather_data('Johannesburg')
    if weather_data:
        print(f"Temperature: {weather_data['main']['temp']}°C")

