import requests
from datetime import datetime, timedelta

# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

hyd_latitude = '17.3946074'
hyd_longitude = '78.4953645'

mnty_latitude = '18.65087'
mnty_longitude = '79.66501'


# Get Hyd weather for past week - 2m_max: 2m above ground level.
hyd_url = f"https://api.open-meteo.com/v1/forecast?latitude={hyd_latitude}&longitude={hyd_longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

mnty_url = f"https://api.open-meteo.com/v1/forecast?latitude={mnty_latitude}&longitude={mnty_longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

hyd_response = requests.get(hyd_url)
hyd_data = hyd_response.json()
print(hyd_data)

mnty_response = requests.get(mnty_url)
mnty_data = mnty_response.json()
print(mnty_data)


