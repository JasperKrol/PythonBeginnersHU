dictonary is een lijst, met key en values en items al objecten

lijst.value()
lijst.item()
lijst.key()

mijn_studenten['Jan']

print(mijn_studenten.items()) alle paren

print(mijn_studenten.key()) namen van keys

print(mijn_studenten.values()) waarden van de keys

    def wie_hebben_er_een_voldoende(studente):
    voldoendes []

    for student, cijfer in studenten.items():
        if cijfer >= 5.5:
            voldoendes.append(student)
        return voldoendes

resultaat = wie_hebben_er_een_voldoende(mijn_studenten)
print(resultaat)

    klaar = False
    while not klaar:
    nieuwe_naam = input('voernaam in')

    if nieuwe_naam in mijn_studenten.keys():
    print('deze bestaat al')
    continue

    if nieuwe naam == "":
    klaar = True
    else:
    nieuwe_cijfer = float(input('voer cijfer in')
    mijn_studenten[nieuwe_naam] = nieuwe_cijfer