import pyowm
import pyowm.utils
import json
import requests

def getCity():
    data = json.loads(requests.get("http://ipinfo.io/json").text)
    return data["city"]

parancs = self.parancs
beszed = self.beszed
if "időjárás" in parancs.lower():
    city = getCity()

    owm = pyowm.OWM("bc12083e70d2d22298c2df1cec7101d9")
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(city)
    w = observation.weather
    temperature = w.temperature('celsius')['temp']

    beszed(f"A {city}i hőmérséklet {temperature} celsius fok")
    quit()