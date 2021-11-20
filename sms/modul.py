import os
import json
import re

def smsKuldes(telefonszam, uzenet):
    os.system(f"""kdeconnect-cli --send-sms "{uzenet}" --destination {telefonszam} --device e3d5c6a284a0e008""")
def telefonszamLekeres(kisbetusnev, kontaktok):
    for kontakt in kontaktok:
        if kontakt["name"].lower() == kisbetusnev:
            return kontakt["number"].replace(" ", "") 
beszed = self.beszed
parancs = self.parancs
h = self.h
hangFelismeres = self.hangFelismeres
kontaktok = json.loads(open("konfiguraciok/kontaktok.json", "r").read())

if "üzenet" in parancs.lower() or "küld" in parancs.lower() or "ír" in parancs.lower():
    if "küldj egy üzenetet" == parancs.lower():
        # nincs személynév specifikálva
        beszed("Kinek szeretnél üzenetet küldeni?")
        szemelynev = hangFelismeres("Kinek szeretnél üzenetet küldeni? ")
        os.remove("hang.wav") # töröljük a (már elemzett) hangfájlt
    elif bool(re.search("^küldj.*egy üzenetet$", parancs.lower())):
        # a személynév a parancs közepén van specifikálva
        varos = h.stem(parancs.split()[1])[0] 
    else:
        # van személynév specifikálva
        szemelynev = parancs.split()[-1]
    stemmedSzemelynev = h.stem(szemelynev)[0]
    telefonszam = telefonszamLekeres(stemmedSzemelynev, kontaktok)
    beszed(f"Mit küldjek el {szemelynev}?")
    uzenet = hangFelismeres(f"Mit küldjek el {szemelynev}? "))
    os.remove("hang.wav") # töröljük a (már elemzett) hangfájlt
    beszed(f"Biztosan elküldjem az üzenetet ({uzenet}) {szemelynev}?")
    elkuldjemE = hangFelismeres(f"Biztosan elküldjem az üzenetet ({uzenet}) {szemelynev}? ")
    os.remove("hang.wav") # töröljük a (már elemzett) hangfájlt
    if elkuldjemE.lower() == "igen":
        smsKuldes(telefonszam, uzenet)
        beszed("Üzenet sikeresen elküldve...")
    else:
        beszed("Üzenet küldése megszakítva...")
    quit()
