import requests
import os
import re

def legkozelebbiAllomas(allomas):
    return Budapest.getNearestStation()
def OpenBubiTelepites():
    openbubiFajl = open("fuggosegek/openbubi.py", "w+")
    openbubiFajl.write(requests.get("https://raw.githubusercontent.com/PiciAkk/OpenBubi/main/openbubi.py").text)
    openbubiFajl.close()

    openbubiFuggosegek = requests.get("https://raw.githubusercontent.com/PiciAkk/OpenBubi/main/requirements.txt").text
    openbubiFuggosegek = openbubiFuggosegek.split()

    pip().telepites(openbubiFuggosegek)

if os.path.exists("fuggosegek/openbubi.py") == False:
    OpenBubiTelepites()

import openbubi

parancs = self.parancs
beszed = self.beszed
h = self.h
hangFelismeres = self.hangFelismeres
credentials = json.loads(open("konfiguraciok/molbubi.json", "r").read())
Budapest = openbubi.BubiMap()
felhasznalo = openbubi.BubiUser(credentials["telefonszam"], str(credentials["pinkod"]))

if "bérlés" in parancs.lower() or "béreld" in parancs.lower() or "bérelj" in parancs.lower():
    if "bérelj ki egy biciklit" == parancs.lower():
        beszed("Mi a biciklin található szám?")
        bicikliSzama = hangFelismeres("Mi a biciklin található szám? ")
        os.remove("hang.wav") # töröljük a (már elemzett) hangfájlt
        bicikliSzama.replace(" ", "")

        beszed(f"Biztosan kibéreljem a biciklit ezzel a számmal: {bicikliSzama}?")
        kibereljemE = hangFelismeres(f"Biztosan kibéreljem a biciklit ezzel a számmal: {bicikliSzama}? ")
        os.remove("hang.wav") # töröljük a (már elemzett) hangfájlt
elif "MOL Bubi" in parancs and "legközelebbi" in parancs.lower() and "állomás" in parancs.lower():
    if "mi a legközelebbi állomás" in parancs.lower() or "mi a legközelebbi mol bubi állomás" in parancs.lower():
        a     
    beszed(f"A legközelebbi állomás a {legkozelebbiAllomas()}")
quit()