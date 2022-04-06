from random import randint


# In de vorige opdrachten heb je een stuk code geschreven dat telt hoeveel klinkers er in een stuk tekst staan
# > Herschrijf dit nu naar een functie die het aantal teruggeeft
# > Voorbeeld:
# >>> print(tel_klinkers('Dit is een string'))
# >>> 5

def tel_klinkers(string):
    aantal_klinkers = 0
    for letter in string:
        if letter in 'aeiuo':
            aantal_klinkers += 1
    return aantal_klinkers


print(tel_klinkers('Dit is een string'))


# > Pas deze functie aan zodat je zelf mee kan geven naar welke letters er gezocht moet worden, en
# dat de functie teruggeeft hoe vaak deze letters (totaal) in de string staan (dus niet per letter).
# > Voorbeeld:
# >>> print(tel_letters('Dit is een string', 's'))
# >>> 2

def tel_letters(string, letters):
    count = 0
    for letter1 in string:
        if letter1 in letters:
            count += 1
    return count


# zin = input('voer je zin in')
# letter = input('welke letter wil je tellen')
#
# getelde_letter = tel_letters(zin, letter)
# print(getelde_letter)

# > Schrijf een functie die als argument een lijst meekrijgt en een lijst teruggeeft met alle even getallen uit de originele lijst
# Voorbeeld:
# >>> print(alleen_even_getallen([1,2,3,4,5,6,7,8]))
# >>> [2,4,6,8]

def alleen_even_getallen(lijst):
    even_getallen = []
    for getal in lijst:
        if getal % 2 == 0:
            even_getallen.append(getal)
    return even_getallen


print(alleen_even_getallen([1, 2, 3, 4, 5, 6, 7, 8]))


# Een pangram is een stuk tekst dat alle letters uit het alfabet bevat: 'The quick brown fox jumps over the lazy dog' is er één, en 'Sphinx of Black Quartz, judge my vow!' ook.
# In het Nederlands 'Pa's wijze lynx bezag vroom het fikse aquaduct' of 'Doch vlakbij zwerft 'n exquis gympje'.
# > Schrijf een functie die als argument een string meekrijgt en checkt of deze een pangram is. Let op hoofdlettergevoeligheid!
# > Voorbeeld:
# >>> print(check_pangram('Dit is een string'))
# >>> False
# >>> print(check_pangram('Doch vlakbij zwerft 'n exquis gympje'))
# >>> True

def check_pangram(string):
    letter = 'abcdefghijklmnopqrstuvwxyz'
    for letter in letter:
        if letter not in string.lower():
            return 'not an pangram'
    return 'this is a pangram'


# zin = check_pangram(input('voer een zin in om te kijken of het een pangram is'))
# print(zin)


# > Maak een functie die checkt of een lijst gesorteerd is.
# > Voorbeeld:
# >>> print(is_gesorteerd([1,5,4]))
# >>> False
# >>> print(is_gesorteerd([1,4,5]))
# >>> True

def is_gesorteerd(lijst):
    for i in range(len(lijst) - 1):
        if lijst[i] > lijst[i + 1]:
            return False
    return True


print(is_gesorteerd([1, 5, 4]))
print(is_gesorteerd([1, 4, 5]))


# > Maak een functie die een lijst met random nummers genereert. Deze functie krijgt mee hoe veel getallen in de
# lijst moeten komen, en tussen welke waardes Gebruik hiervoor de volgende functie: randint Deze kan je importeren
# uit de random library met de volgende regel code: from random import randint  # let op normaal zet je dit bovenaan
# je bestand

def genereer_lijst(aantal, minimaal, maximaal):
    lijst = []
    for _ in range(aantal):
        lijst.append(randint(minimaal, maximaal))
    return lijst


# > Gebruik deze twee laatste functies om net zolang lijsten van 10 nummers tussen de 0 en 5 te genereren tot er een
# gesorteerde lijst uit komt. Print deze lijst.

lijst = genereer_lijst(10, 0, 5)
while not is_gesorteerd(lijst):
    lijst = genereer_lijst(10, 0, 5)

print(lijst)
