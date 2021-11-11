import requests
import json

def idojaras(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=1a9a4d9f4f8f8a9a8d9f7c1d0c0e8c8f"
    return json.dumps(requests.get(url).text)

parancs = self.parancs
if "időjárás" in parancs.lower():
    print(idojaras("Budapest"))