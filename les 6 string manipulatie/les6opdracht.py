
# `text` bevat een hele lange string (het hele script voor Bee Movie)
print(len(text))

# > Tel hoe vaak het woord 'bee' (of 'Bee', of 'BEE' etc. ) voorkomt in deze tekst
# Hint: Je kunt de hele string hoofdletters of kleine letters te maken, dan hoef je niet voor elke variatie op het woord 'bee' te checken.
lower_text = text.lower()

amount_bee = 0
if text.find("bee"):
    amount_bee = text.count("bee")

print(f' text bevat {amount_bee} keer bee')

# > Wat is de eerste plek waar het woord 'bee' staat?
eerste_bee = None
if text.count('bee'):
    eerste_bee = text.find('bee')
print(f'index eerste bee {eerste_bee}')

# > Wat is de laatste plek waar het woord 'bee' staat?
# doormiddel van reverse find
laatste_bee = None
if text.count('bee'):
    laatste_bee = text.find('bee')
print(f'index laatste bee {laatste_bee}')

# > Tel, door middel van een for loop, hoeveel klinkers er in het script staan
# Dit kun je doen door voor elke letter te kijken of het een klinker is

aantal_klinkers = 0
for letter in text:
    if letter in 'aeiuo':
        aantal_klinkers += 1
print(f'{aantal_klinkers} klinkers in de text')

# > Kijk, door middel van een for loop, of er een cijfer in het script staat. Gebruik hiervoor de ingebouwde isnumeric() functie
if letter in text:
    if letter.isnumeric:
        print('ja er zitten cijfers is')
    else:
        print('helaas geen cijfers')

# > Tel ook hoeveel nummers er in het script staan

aantal_cijfers = 0
for letter in text:
    if letter.isnumeric:
        aantal_cijfers += 1
print(f'er zitten {aantal_cijfers} cijfers in de text')

# > Tel hoeveel woorden beginnen met de lettercombinatie 'be'. Hiervoor is het nodig om de string eerst te splitten, daarna kun je kijken welke woorden beginnen met deze letters.
split_text = text.split()
be_counter = 0

for word in split_text:
    if word.startswith('be'):
        be_counter += 1
print(f'aantal woorden met be {be_counter}')

# > Vervang d.m.v. een for loop elke instantie van het woord 'bee' door het woord 'duck'. Gebruik hiervoor de lijst die je bij de vorige opdracht gemaakt hebt.

# gespleten text is nu in arraylist
# over de arraylist heen loopen en het vervangen

for i in range(len(split_text)):
    if split_text[i] == 'bee':
        split_text[i] = 'duck'

# > Gebruik de join() functie om het weer naar één verhaal terug te zetten.
new_text = " ".join(split_text)
