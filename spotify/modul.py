import os

beszed = self.beszed
parancs = self.parancs
h = self.h
hangFelismeres = self.hangFelismeres

if "állítsd meg" in parancs.lower() or "állítsd le" in parancs.lower():
    os.system("spotifycli --pause")
    beszed("Zene sikeresen leállítva")
    quit()
elif "indítsd el" in parancs.lower():
    os.system("spotifycli --play")
    beszed("Zene sikeresen elindítva!")
    quit()