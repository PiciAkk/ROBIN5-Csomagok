import datetime
import pytz

def getCity():
    data = json.loads(requests.get("http://ipinfo.io/json").text)
    return data["city"]
currentDT = datetime.datetime.now()
currentTime = currentDT.strftime("%H:%M:%S")

print(currentDT)
print(currentTime)

parancs = self.parancs
beszed = self.beszed
h = self.h
hangFelismeres = self.hangFelismeres

if "mennyi az idő" in parancs.lower() or "hány óra van" in parancs.lower():
    if "mennyi az idő" == parancs.lower() or "hány óra van" == parancs.lower():
        varos = getCity()
        ido = datetime.datetime.now().strftime("%H:%M:%S")
    else:
        varos = h.stem(parancs.split()[-1])[0]
        idozona = pytz.timezone(varos)
        ido = datetime.datetime.now(tz).strftime("%H:%M:%S")
    beszed(f"A {varos}i idő {ido}")
