parancs = self.parancs
if "időjárás" in parancs.lower():
    owm = pyowm.OWM("bc12083e70d2d22298c2df1cec7101d9")
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place("Hungary, Budapest")
    w = observation.weather

    self.beszed(w.temperature("celsius")["temp"])
    quit()