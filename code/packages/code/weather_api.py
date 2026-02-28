import requests


# We need coordinates to get weather data
latitude = 17.3946074 
longitude = 78.4953645

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()
status_code = response.status_code

print(data)
print(status_code)

print(type(data))

data.keys()

data["current"]
temperature = data["current"]["temperature_2m"]
