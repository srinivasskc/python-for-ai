import requests
import pandas as pd
import matplotlib.pyplot as plt
import os

from datetime import datetime, timedelta

# Check current working directory.
print(os.getcwd())


# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

hyd_latitude = '17.3946074'
hyd_longitude = '78.4953645'

# Get Hyd weather for past week - 2m_max: 2m above ground level.
hyd_url = f"https://api.open-meteo.com/v1/forecast?latitude={hyd_latitude}&longitude={hyd_longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

hyd_response = requests.get(hyd_url)
hyd_data = hyd_response.json()
print(hyd_data)

#######################
# Organize the data - load into pandas

# Get Daily data.
daily_data = hyd_data['daily']

df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']    
})

print(df)

# Calculate average temperature.
df['avg_temp'] = (df['max_temp'] + df['min_temp'])/2

# Convert date strings to datetime.
df['date'] = pd.to_datetime(df['date'])

print(df)

############################

# Visualize the data


# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')
plt.plot(df['date'], df['avg_temp'], marker='o', label='Average Temp')


# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Hyd Weather - Past 7 Days')
plt.legend()

# Add grid
# grid - visible: True, alpha - transparency opacity. 
# Less opacity - No grid visible, More opacity - visible
plt.grid(visible=True,alpha=0.3)


# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('../output/weather_chart.png')
plt.show()



# Create data folder if it doesn't exist
if not os.path.exists('../data'):
    os.makedirs('data')

# Save to CSV
df.to_csv('../data/hyd_weather.csv', index=False)
print("Data saved to data/hyd_weather.csv")


# Check if weather data file exists
data_path = "../data/hyd_weather.csv"
if os.path.exists(data_path):
    print(f"✅ Found {data_path}")
else:
    print(f"❌ Cannot find {data_path}")
    print("Make sure you're running from the sales-analysis folder!")

