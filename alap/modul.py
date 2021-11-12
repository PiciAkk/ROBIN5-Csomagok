parancs = ROBIN().parancs
beszed = ROBIN().beszed

if "szia" in parancs.lower() or "hello" in parancs.lower() or "köszöntelek" in parancs.lower() or "helló" in parancs.lower():
    beszed("Köszöntelek! ROBIN vagyok!")
    quit()