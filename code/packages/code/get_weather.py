import requests

def get_weather(latitude,longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
    response = requests.get(url)
    data = response.json()
    return data["current"]["temperature_2m"]

hyd_temp = get_weather('17.3946074','78.4953645')
bang_temp = get_weather('12.973646509947548','77.74373717118257')
print(f"Hyderabad Weather: {hyd_temp}°c")
print(f"Bangalore Weather: {bang_temp}°c")
