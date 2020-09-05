import requests, json

api_key = "741ac955b4c0f99f58c5c61b780e953e"
lat = "12.9166"
lon = "77.6101"
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)

response = requests.get(url)
data = json.loads(response.text)
print(data)


