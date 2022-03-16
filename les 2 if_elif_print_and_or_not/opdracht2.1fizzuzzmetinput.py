# Vraag de gebruiker om een getal in te voeren
# Zorg ervoor dat je dit ook echt als getal kunt gebruiken

# Als het getal deelbaar is door 3:     print fizz
# Als het getal deelbaar is door 5:     print buzz
# Als het getal deelbaar is door 3 & 5: print fizz én buzz
# Anders print je het getal

# Voorbeeld:
# Gebruiker geeft het getal 12 in
# 12 is deelbaar door 3 (12/3 = 4), dus 'fizz' wordt geprint
# 12 is niet deelbaar door 5 (12/5 = 2.4), dus 'buzz' wordt niet geprint
# Omdat 12 deelbaar is door 3 hoeft het getal zelf niet geprint te worden.

# Voor de getallen 1 t/m 5:
# 1 -> 1
# 2 -> 2
# 3 -> 'fizz'
# 4 -> 4
# 5 -> 'buzz'

numbers = int(input('Voer een getal naar wens in\n'))
print(f'je hebt voor het getal {numbers} gekozen\n')

for numbers in range(numbers + 1):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print('FizzBuzz')
        continue
    elif numbers % 3 == 0:
        print("Fizz")
        continue
    elif numbers % 5 == 0:
        print('Buzz')
        continue
    else:
        print(numbers)
