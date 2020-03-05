"""
Går igenom Mock i unittest.
https://docs.python.org/3/library/unittest.mock.html
"""
from unittest import mock

# Skapar magiskt objekt
# https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock
# MagicMock är en subklass till Mock. Mock objekt skapar attribut och metoder
# när de används på objektet och sparar hur de har använts. Det går även
# att konfigurera dem för att sätta retur värden och assert:a hur de har använts
m = mock.MagicMock()
# Om anropar m som en funktion ska den returnera "magic"
m.return_value = "magic"

print(m())

def foo():
    return "functional magic"

# Om side_effect är satt till en funktion som returnerar ett värde kommer 
# det värdet returneras och inte värdet från ".return_value".
m.side_effect = foo
print(m())

# side_effect kan också vara en sekvens
m.side_effect = [1, 2, 3]
# Då returveras nästa element varje gång mocken anropas.
print(m())
print(m())
print(m())
# Kastar StopIteration
# print(m())



# Vi kan lägga till attribut på Mock objektet också
m.something = "magic"
print(m.something)

# Låtsas skapa funktioner och bestämma vad de ska returnera
m.foo.return_value = "funcational magic"
print(m.foo())

# Vi kan göra väldigt mycket och dynamiska saker med Mock.