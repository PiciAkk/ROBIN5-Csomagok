import pyowm
import pyowm.utils
import json
import requests

def getCity():
    data = json.loads(requests.get("http://ipinfo.io/json").text)
    return data["city"]

parancs = self.parancs
beszed = self.beszed
h = self.h
hangFelismeres = self.hangFelismeres

if "időjárás" in parancs.lower() or "hőmérséklet" in parancs.lower() or "hány fok van" in parancs.lower():
    if "milyen az időjárás" == parancs.lower() or "milyen a hőmérséklet" == parancs.lower() or "hány fok van" == parancs.lower():
        varos = getCity()
    else:
        varos = h.stem(parancs.split()[-1])[0]

    owm = pyowm.OWM("bc12083e70d2d22298c2df1cec7101d9")
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(varos)
    w = observation.weather
    homerseklet = w.temperature('celsius')['temp']

    beszed(f"A {varos}i hőmérséklet {homerseklet} celsius fok")
    quit()
