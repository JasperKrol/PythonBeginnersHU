# Bekijk je fizzbuzz van vorige week.
# Nu willen we fizzbuzz voor alle getallen van 1 tot en met 100 uitvoeren 
# Met input zou dit te lang duren ;)
# Schrijf dit nu met een loop, zodat dit automagisch gebeurt
getal = 32

for i in range(getal):
    if i % 3 == 0 and getal % 5 == 0:
        print('FIZZBUZZ')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
# print alle even getallen vanaf 0 tot en met 42; gebruik hiervoor geen modulo!
for getal in range(0, 43, 2):
    print(getal)
# Schrijf een loop die een driehoek van sterretjes print, zoals
# *
# * *
# * * *
# etc.
# Doe dit tot 10 sterretjes.
for stars in range(1, 11):
    print('* ' * stars)
print()

# Laat je driehoek nu ook weer terug lopen.
# *
# * *
# (.. meer sterren ..)
# * *
# *
# Hint: gebruik twee for loops

for stars in range(0, 11):
    print('* ' * stars)
for stars in range(9, 0, -1):
    print('* ' * stars)

# Voor een extra uitdaging bij deze opdracht kan je de driehoek ook zo maken (doe dit pas als je de rest af hebt. Let op: is erg lastig):
#   *
#  * *
# * * *

grootte = 10
for i in range(grootte):
    print((grootte - i) * ' ' + i * '* ')



# Schrijf nu je eigen max algoritme; zoek het grootste getal uit onderstaande lijst
# Je mag er vanuit gaan dat het kleinste getal nul is.
#
# Stappen:
# Maak een var_max met als waarde nul
# Loop over de lijst heen
# Als de waarde groter is dan var_max maak de variabele deze waarde
#
# Check of jouw max overeenkomt met de max van de python functie max()


lijst = [1, 3, 4, 1, 123, 0, 5, 1, 32, 1, 1, 3, 5, 1, 125, 3, 101, 10]

max_value = 0
for getal in lijst:
    if getal > max_value:
        max_value = getal
        print(max_value)

print(max_value)
