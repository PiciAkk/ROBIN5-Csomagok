import pyowm
import pyowm.utils
import json

parancs = self.parancs
beszed = self.beszed
if "időjárás" in parancs.lower():
    owm = pyowm.OWM("bc12083e70d2d22298c2df1cec7101d9")
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place("Hungary, Budapest")
    w = observation.weather

    beszed(f"A Budapesti hőmérséklet {w.temperature("celsius")["temp"]} celsius fok")
    quit()