import os

beszed = self.beszed
parancs = self.parancs
h = self.h
hangFelismeres = self.hangFelismeres

if "állítsd meg" in parancs.lower():
    os.system("spotifycli --pause")
elif "indítsd el" in parancs.lower():
    os.system("spotifycli --play")