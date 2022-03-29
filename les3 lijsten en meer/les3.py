onze_lijst = [14592, 3278, 36048, 32098, 29256, 18289, 13434, 11395, 55302, 4165, 3905, 12280, 28657, 30495, 3478,
              26062, 54987, 28893, 58878, 36463, 851, 20926, 55392, 44597, 36421, 20379, 28221, 44118, 13396, 12156,
              49797, 12676, 47052, 45082, 34671, 5695, 60217, 16361, 49615, 10328, 38427, 47400, 25203, 9116, 6006,
              29871, 37930, 10458, 30512, 13238, 49823, 36434, 59429, 47819, 21319, 48520, 46566, 27460, 34993, 9358,
              22431, 32087, 21417, 60589, 49735, 35382, 28785, 42504, 7331, 30021, 4207, 41347, 52581, 35093, 8675,
              27653, 41245, 27869, 65435, 51856, 60142, 18726, 34718, 18301, 32325, 34438, 56155, 52350, 47447, 28746,
              18131, 64686, 11915, 6175, 14371, 20033, 20969, 55333, 8326, 50432]

# > Bereken de som van de lijst genaamd 'onze_lijst'.
# Deze lijst is gevuld met unieke, willekeurige getallen
print(type(onze_lijst))
print(type(onze_lijst[0]))

# > Bereken ook het gemiddelde van de elementen in deze lijst
amount = len(onze_lijst)
sumOfList = sum(onze_lijst)
print(
    f'f de lijst heeft {amount} variablen in zich en de som van deze getallen is {sumOfList}\n het gemiddelde is {sumOfList / amount}')

# > Bekijk of het element op index 5 groter is dan het gemiddelde
gemiddelde = sum(onze_lijst) / len(onze_lijst)

fifth_element = onze_lijst[5]
if fifth_element > gemiddelde:
    print(f'Het vijfde element ({fifth_element}) is groter dan het gemiddelde ({gemiddelde})')
else:
    print(f'Het vijfde element ({fifth_element}) is niet groter dan het gemiddelde ({gemiddelde})')

# > Wat is het laatste element in de lijst?
lastElement = onze_lijst[-1]
print(f' last element is: {lastElement}')

# > Als je dit nog niet gedaan had: bekijk dit door naar het laatste element in de lijst te kijken zonder de lengte van de lijst te gebruiken.

# > Wat is het grootste getal in de lijst? Vraag de index op van dit getal
grootste_getal = max(onze_lijst)
gr_getal_index = onze_lijst.index(grootste_getal)
print(f'Het grootste getal in de lijst is {grootste_getal} en is te vinden op plaats {gr_getal_index}')

# > Plaats voor en na dit getal een 0.
onze_lijst.insert(gr_getal_index, 0)
print(onze_lijst[78])
onze_lijst.insert(onze_lijst.index((max(onze_lijst)))+1, 0)
print(onze_lijst)

# Dus als 10 het grootste getal is wordt de lijst [..., 0, 10, 0, ...]
# > Zoek het grooste nummer deze keer in de lijst door de lijst te sorteren en naar het laatste element te kijken - hiervoor kun je een functie gebruiken. Vergelijk dit met het grootste nummer dat je eerst vond.
# Draai de lijst om, zodat nu het kleinste getal achteraan staat. Controleer dit door te kijken of het eerste element nog steeds het grootste element is.

onze_lijst.sort()
grootsteGetalNaSort = onze_lijst[-1]
print(f'grootsteGetalNaSort {grootsteGetalNaSort}')

onze_lijst.reverse()
grootsteGetalNaReverse = onze_lijst[0]

if grootsteGetalNaReverse == grootsteGetalNaSort:
    print("yes het is nog het zelfde")
else:
    print('iets klopt er nog niet')
# > Maak nu de lijst leeg
onze_lijst.clear()
print(f'onze lijst leeg? {onze_lijst}')

# > Maak een string en vul deze met minimaal 20 letters (hoeft geen bestaand woord o.i.d. te zijn)
randomString = 'ikbeneenrandomstring'
# > Vraag met input om een letter en tel hoe vaak die letter in de lijst staat
# letter = input(f'voer een letter in om te kijken hoevaak deze voorkomt\n')
# print(f'je hebt de letter {letter} gekozen')
# amountInWord = randomString.count(letter)
# print(f'the letter is {amountInWord} times in the word')


# Hieronder een lijst met wachtwoorden:
wachtwoorden = ['wachtwoord', '1234', '0000', 'mijn_verjaardag', 'naam_van_huisdier', 'qwerty', 'admin', 'wachtw00rd']

# > Vraag een gebruiker om zijn gebruikersnummer (dat is de index (positie) in de lijst)
gebruikerID = int(input('wat is je user ID ?\n'))

# > Vraag een gebruiker om zijn wachtwoord
wachtwoordUser = input('voer je wachtwoord in\n')
# > Kijk of het wachtwoord klopt
if wachtwoordUser == wachtwoorden[gebruikerID]:
    print('wachtwoorden komen overeen')
else:
    print('helaas komen niet overeen')
# > Laat de gebruiker het wachtwoord aanpassen
nieuw_wachtwoord = input('voer nieuw wachtwoord op')
wachtwoorden[gebruikerID] = nieuw_wachtwoord
# > Sla deze aanpassing op de goede plek in de lijst op
# > Controleer of het wachtwoord veranderd is
if wachtwoorden[gebruikerID] == nieuw_wachtwoord:
    print('opgeslagen en wel')
else:
    print('niet gelukt met opslaan')
