import requests

openbubiFajl = open("fuggosegek/openbubi.py", "w+")
openbubiFajl.write(requests.get("https://raw.githubusercontent.com/PiciAkk/OpenBubi/main/openbubi.py").text)
openbubiFajl.close()

openbubiFuggosegek = requests.get("https://raw.githubusercontent.com/PiciAkk/OpenBubi/main/requirements.txt").text
openbubiFuggosegek = openbubiFuggosegek.split()

pip().telepites(openbubiFuggosegek)

import openbubi

