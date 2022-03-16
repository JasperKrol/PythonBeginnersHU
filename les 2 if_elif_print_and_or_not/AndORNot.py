"""
Er zijn 3 grote 'logische' operatoren; AND, OR en NOT

De makkelijkste van deze 3 is de NOT, in Python simpelweg geschreven als 'not'

NOT kijkt naar wat er rechts van zich staat en draait dat om:
"""

print(f'Het omgedraaide van True is: {not True}')
print(f'Het omgedraaide van False is: {not False}\n')

"""
We hadden eerder al gezien dat expressies (zoals '3>2') ook eigenlijk True of False (booleans) teruggeven:
"""

print(f'Is 3 groter dan twee?: {3>2}')

"""
En ook de uitkomsten van deze expressies kun je dus omdraaien:
"""

print(f'Het omgedraaide van 3>2: {not (3>2)}\n')

"""
Hierna krijg je de AND, in Python geschreven als 'and'

AND kijkt naar expressies zowel links als rechts van zichzelf en geeft True terug als beide expressies ook True teruggeven:
"""

print(f'True and True: {True and True}')
print(f'True and False: {True and False}')
print(f'False and True: {False and True}')
print(f'False and False: {False and False}\n')

"""
Dit kun je dus ook gebruiken voor complexere expressies:
"""

print(f'3 is groter dan 2 EN 10 is kleiner dan 12: {(3>2) and (10<12)}')

"""
3>2 geeft True terug, 10<12 geeft ook True terug, en True and True was, zoals eerder gezien, ook True.

De vergelijkingen die hier nu staan kun je vervangen met bijna alles wat we eerder al gezien hebben:
"""

naam = "Nick" # Kan natuurlijk ook met input
leeftijd = 28

print(f"Naam bevat Nick en leeftijd is kleiner óf gelijk aan 28: {('Nick' in naam) and (leeftijd <= 28)}\n")

"""
OR, in Python 'or', werkt bijna hetzelfde als AND, behalve dat maar één van de twee expressies True hoeft te zijn om True terug te geven (maar beide mag natuurlijk ook):
"""

print(f'True or True: {True or True}')
print(f'True or False: {True or False}')
print(f'False or True: {False or True}')
print(f'False or False: {False or False}\n')

"""
En verder kun je hier dus voor links en rechts net als bij AND heel veel verschillende dingen schrijven.

Als laatste kun je al deze logische operatoren ook nog met elkaar combineren:
"""

print(f'True or True and False: {True or False and True}\n')

"""
In de regel bekijkt Python dit van links naar rechts:
True and False geeft False terug, en dan bekijkt hij die False voor de 'or True', wat True teruggeeft.

Als je een andere volgorde wilt kun je, net als in wiskunde, haakjes gebruiken. En ook hier kun je dus bijvoorbeeld de NOT toepassen:
"""
print(f'False or not True and False: {False or not True and False}')
print(f'False or not (True and False): {False or not (True and False)}\n')

"""
In dit geval berekent Python eerst wat tussen de haakjes staat en gaat dan verder.

Zo kun je dus de uitkomst van een expressie veranderen als je per se een bepaalde volgorde wilt forceren.

En al deze logische operatoren kun je natuurlijk ook in IF statements e.d. gebruiken:
"""

if ("Nick" in naam) and (leeftijd <= 28):
    print("Er zit Nick in je naam en je leeftijd is kleiner of gelijk aan 28")
else:
    print("Er zit óf geen Nick in je naam, óf je leeftijd is te hoog, óf allebei ¯\_(ツ)_/¯")