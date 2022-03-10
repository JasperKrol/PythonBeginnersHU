## LOGICA

# Verander de vergelijkingsoperator zodat de print uitgevoerd wordt

# Voorbeeld:
x = 5
if x == 4:  # 5 == 4 = False, dus de print wordt nu niet uitgevoerd
    print(x)

# Wordt:
x = 5
if x != 4:  # 5 != 4 = True, dus nu wordt er wel geprint
    print(f'oefening 1 {x}')

z = 5
if not (z < 4):
    print(f'oefening 2 {z}')

if z == x:
    print(f'oefening 3 {z}')

if z + 2 > 3:
    print(f'oefening 4 {z}')

if z > 3 != 2:
    print(f'oefening 5 {z}')

## STRINGS

# naam = input('Wat is je naam? ')
# print(f'klopt het dat je naam {naam} is?')
# salaris = int(input('Hoeveel heb je deze maand verdiend? '))
# print(f'je hebt {salaris} verdiend deze maand, dik ')
# uurloon = int(input('Hoeveel krijg je per uur? '))
# print(f'je krijgt {uurloon} per uur, dat is {salaris/uurloon} uur deze maand!')

# > print nu met 'f'-strings  de naam van deze pesoon, hoeveel deze persoon verdiend heeft, het uurloon en hoeveel uren deze persoon dus gewerkt heeft.

# > Vraag een gebruiker in welk jaar deze persoon geboren is
# > Vraag ook welk jaar het nu is
# > Bereken hoe oud deze persoon is, en print zo vaak 'HOERA!' door middel van een f-string
# birthYear = int(input("Wat is je geboorte jaar?\n"))
# currentYear = int(input("Welk jaar is het n\n"))
# print(f'klopt het dat je {currentYear-birthYear} jaar bent?\n feliciaties:')
# age = currentYear-birthYear
#
# for birthday in range(age):
#     print("hoera!")

# > Vraag een gebruiker om een woord in te typen
# > Vraag de gebruiker ook om een letter in te geven
# > Print of de gegeven letter in het woord voorkomt
# givenWord = input('vul een woord in\n')
# letterInWord = input('voer een letter in\n')
# if letterInWord in givenWord:
#     print(f'the letter {letterInWord} is in {givenWord}')
# else:
#     print(f'the letter {letterInWord} is not in the word {givenWord}')

# Maak een super slecht wachtwoord programma.
# > Vraag een gebruiker om een wachtwoord in te stellen
# > Vraag een gebruiker om het wachtwoord te herhalen
# > Kijk of deze overeenkomen
# > Sla het wachtwoord op in een variabele
password = input('Please enter your password\n')
print(f'{password}')
confirmPassword = input('Re-enter your password\n')
print(f'{confirmPassword}')
if password != confirmPassword:
    print("Passwords does not match")
else:
    setPassword = password
    print(f'password {setPassword}')
