import os

beszed = self.beszed
parancs = self.parancs
h = self.h
hangFelismeres = self.hangFelismeres

if "nyisd meg" in parancs.lower():
    alkalmazas = h.stem(parancs.split()[-1])[0]
    if alkalmazas == "terminál":
        os.system("xfce4-terminal")
    else:
        os.system(alkalmazas)
    beszed(f"{alkalmazas} sikeresen megnyitva")
    quit()