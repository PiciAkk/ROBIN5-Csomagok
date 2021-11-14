import os

beszed = self.beszed
parancs = self.parancs
h = self.h
hangFelismeres = self.hangFelismeres

if "állítsd meg" in parancs.lower() or "állítsd le" in parancs.lower():
    os.system("spotifycli --pause")
    beszed("Zene sikeresen leállítva")
    quit()
elif "indítsd el" in parancs.lower() or "játssz le" in parancs.lower() or "rakj be" in parancs.lower():
    os.system("spotifycli --play")
    beszed("Zene sikeresen elindítva!")
    quit()
elif "ugorj a következő" in parancs.lower():
    os.system("spotifycli --next")
    beszed("Következő zene!")
    quit()
elif "ugorj az előző" in parancs.lower():
    os.system("spotifycli --prev")
    beszed("Előző zene!")
    quit()