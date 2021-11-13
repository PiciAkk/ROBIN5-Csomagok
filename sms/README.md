# SMS
ROBIN SMS csomag

## Telepítés

```bash
./robin.py telepítés sms
```

## Függőségek

Ennek a csomagnak az egyetlen függősége a KDE Connect

## Konfiguráció

A csomag használatához be kell konfigurálnod a kontaktjaidat. Ehhez hozz létre egy `kontaktok.json` fájlt ROBIN `konfiguraciok` mappájában. Ebbe a fájlba kell beírni a kontaktokat, amikhez a csomag hozzáférhet.

Amint az alábbi példában is látható, a kontaktokat JSON formátumban kell megadni. Ezeket egy arrayben kell elhelyezni, ahol minden kontakt egy JSON objektum. Az objektumnak a következő kulcsai kell, hogy legyenek: `name` és `number`. A `name` a kontakt neve, a `number` pedig a kontakt telefonszáma.

```json
[
    {
        "name": "Kontakt 1",
        "number": "123 456 789"
    },
    {
        "name": "Kontakt 2",
        "number": "987 654 321"
    }
]
```

Amint a felőbb