# hidden.py geeft jullie een geheim nummer genaamd `secret_number`, dit is iedere keer dat je het runt anders. Schrijf een programma met een while loop welke de gebruiker 3 pogingen geeft om het getal te raden. Als de gebruiker het getal niet goed raad vertel dan of het groter of kleiner is dan het geheime getal
# hint gebruik de if,elif,else constructie die we hebben geleerd

# tries = 0
# while tries < 3:
#     guess = int(input(f"gok {tries + 1}, gok een nummer tussen 0 en 10: "))
#     if guess > secret_number:
#         print("Het getal is kleiner dan je gok")
#     elif guess < secret_number:
#         print("Het getal is groter dan je gok")
#     else:
#         print("Goedzo")
#         break
#     tries = tries + 1
# if tries == 3:
#     print('you lose')

#      _  _  __
#  ___(_)(_)/ _| ___ _ __ ___
# / __| || | |_ / _ \ '__/ __|
# | (__| || |  _|  __/ |  \__ \
# \___|_|/ |_|  \___|_|  |___/
#      |__/

# > Vraag een gebruiker d.m.v. een while loop om cijfers van zijn studenten (komma getallen van 1 t/m 10)
# > Sla deze op in een lijst
# > Als de gebruiker 0 invoert is hij klaar met de lijst.
from random import shuffle

cijfers = []
cijfer = -1.0

while cijfer != 0.0:
    cijfer = float(input('vul een cijfer in om de lijst te vullen\n'))
    if cijfer < 0 or cijfer > 10:
        print(f'ongeldige invoer voor {cijfer}')
        continue
    cijfers.append(cijfer)

# Nu we een lijst van cijfers hebben kunnen we daar dingen voor berekenen
# > Bereken met behulp van een for loop het aantal elementen in de lijst:
# > maak een variabele voor de lengte
lengte = 0

for cijfer in cijfers:
    lengte += 1

# print(f'de lijst bevat {lengte} cijfers')


# > Bereken door een for loop te gebruiken het gemiddelde van de cijfers:

# > maak een variabele
# > gebruik een for loop om daar ieder cijfer bij op te tellen
# > als dat klaar is deel het door het aantal getallen in de lijst
totaal = 0
for cijfer in cijfers:
    totaal += cijfer
gemiddelde = totaal/lengte

# > Bereken door één for loop te gebruiken de volgende drie dingen: hoeveel voldoendes er zijn, het minimum en het maximum in de lijst:
# > Gebruik drie variabelen een voor de hoeveelheid voldoendes, een voor het minimum en een voor het maximum
# > Gebruik in je for loop drie if statements (een voor het minimum en een voor het maximum)
voldoendes = 0
maximum = 0
minimum = 11

for cijfer in cijfers:
    if cijfer < minimum:
        minimum = cijfer
    if cijfer > maximum:
        maximum = cijfer
    if cijfer >= 5.5:
        voldoendes += 1

print(f'aantal cijfers {lengte}')
print(f'Het gemiddelde cijfer {gemiddelde}')
print(f'Het minimum cijfer is {minimum} en het maximale cijfer: {maximum}')
print(f'er zijn {voldoendes} voldoendes behaald')

# > print nu de statistieken over deze cijfers die je net hebt berekend

#      _            __  __ _
#  ___| |__  _   _ / _|/ _| | ___
# / __| '_ \| | | | |_| |_| |/ _ \
# \__ \ | | | |_| |  _|  _| |  __/
# |___/_| |_|\__,_|_| |_| |_|\___|
#

# shuffle sort
# shuffle sort is een van de minst efficiente sort algoritmen dat er is
# het gaat als volgt te werk:
# > Neem een lijst met getallen (bijvoorbeeld de lijst die je in de vorige opdracht hebt gemaakt)
# > Shuffle deze random door elkaar (als het schudden van een pakje kaarten)
# > Kijk of de lijst gesorteerd is
# > Is de lijst gesorteerd ben je klaar, is deze niet gesorteerd shuffle dan nog een keer
#
# Wij hebben de lastigere onderdelen al geschreven voor jullie:
# gebruik de volgende functie om te kijken of een lijst gesorteerd is
# `is_sorted(lijst)` > Deze returnt True als de lijst gesorteerd is en False als dat niet het geval is.
# gebruik deze functie om een lijst te schudden
# `shuffle(lijst)` > deze verandert de bestaande lijst


while not is_sorted(cijfers):
    print(cijfers)
    shuffle(cijfers)
print(cijfers)
#
# Om te kijken hoe het sorteren gaat kan je tussendoor je lijst printen
