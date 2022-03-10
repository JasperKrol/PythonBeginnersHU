# Met de type(variabele) functie kun je het type van een object achterhalen.
# Welke types hebben de volgende objecten? Tip: Probeer het eerst zelf te bedenken, voordat je het met de functie controleert
#Voorbeeld:
var1 = "Test"
type(var1)
# >> <class 'str'>, dit is dus een string

a = 6
b = "Hello World"
c = 2.0
d = True

# Als we nu het volgende toevoegen
a = b
# Welke types hebben a en b dan?

e = a == b
a = 6
f = a > c

# Doe hetzelfde voor de volgende expressies, maar probeer ook te bedenken wat de resultaten van de expressies zouden moeten zijn.
# Wederom; probeer dit eerst zelf te bedenken voordat je het laat berekenen door Python

g = 4 + 23
h = 12 + 0.5
i = 1.0 - 1.0

j = 2 * 5
k = 2.0 * 10
l = k - 1.0

m = 10 / 2
n = 11 / 4
o = 11 // 4
print(n)
print(o)
p = 8**2
q = 2**8
r = 15 % 3
s = 3 % 15
print('r', r)
print('s', s)
t = 20 % 8

u = 24
v = 12
u = v = 42
w = u != v
print(u)
print(v)
print(w)

x = 2+3*9+3**3/6
