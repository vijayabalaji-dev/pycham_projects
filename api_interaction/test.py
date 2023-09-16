import requests

MY_LAT = 12.9107772
MY_LONG = 77.6782101

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG
}

response = requests.get(url=f'https://api.sunrise-sunset.org/json/', params=parameters)
response.raise_for_status()
data = response.json()
print(data)
