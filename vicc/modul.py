import random

semleges = [
    "- Miért keveri a programozó a Halloween-t a Karácsonnyal? - ??? - Mert az egyik oct 31 a másik meg dec 25.",
    "Két programozó beszélget: - Milyen a kedved? - Egész változó... - Integer???",
    "- Mire táncolnak a programozók a buliban? - Algoritmusra.",
    "10-féle ember létezik. Az egyik ismeri a bináris számrendszert, a másik nem.",
    "- Hogyan próbálnak meggazdagodni az objektumorientált programozók? - ??? - Öröklődés által.",
    "- Mi a teendő tűz esetén? - ??? - 1. `git add .` 2. `git commit` 3. `git push` 4. hagyjuk el az épületet",
    "- Mit csinál a backend fejlesztő, amikor sikeresen megváltoztat valamit CSS-ben? - ??? - Beírja az önéletrajzába, hogy full stack fejlesztő",
    "- Hogy hívsz nyolc hobbitot? - ??? - Egy hobbyte."
]

chuck = [
    "- Miért Chuck Norris a világ legjobb programozója? - ??? - Mert olyan kódot ír, ami saját magát képes optimalizálni."
]

osszes = semleges+chuck

def randomVicc(category):
    if category == "barmilyen":
        return random.choice(osszes)
    elif category == "semleges":
        return random.choice(semleges)
    elif category == "chuck":
        return random.choice(chuck)

hangFelismeres = self.hangFelismeres
parancs = self.parancs
beszed = self.beszed
h = self.h

if "vicc" in parancs.lower():
    beszed(randomVicc("barmilyen"))
    quit()