import datetime
import pytz
import pycountry_convert as pc
from googletrans import Translator
import json
import requests
from geopy.geocoders import Nominatim 

def forditas(szoveg, forrasnyelv, celnyelv):
    translator = Translator()
    return translator.translate(szoveg, src=forrasnyelv, dest=celnyelv).text
def varosLekerese():
    data = json.loads(requests.get("http://ipinfo.io/json").text)
    return data["city"]

parancs = self.parancs
beszed = self.beszed
h = self.h
hangFelismeres = self.hangFelismeres

if "mennyi az idő" in parancs.lower() or "hány óra van" in parancs.lower():
    varos = varosLekerese()
    ido = datetime.datetime.now().strftime("%H:%M:%S")
    beszed(f"A {varos}i idő {ido}")
    quit()
