"""
Går igenom Mock i unittest.
https://docs.python.org/3/library/unittest.mock.html
"""
from unittest import mock
# https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock

# Vi kan antingen skapa ett Mock eller MagicMock objekt.
# För att använda Mock objektet behöver vi i förväg specificera vilka attribut
# och metoder som ska ersättas och hur de ska betee sig.
# MagicMock däremot är mer automatisk/magisk, det objektet har vissa metoder förskapade.

# MagicMock är en subklass till Mock. Objekt skapar attribut och metoder
# när de används på objektet och sparar hur de har använts. Det går även
# att konfigurera dem för att sätta retur värden och assert:a hur de har använts
m = mock.MagicMock()
# Om anropar m som en funktion ska den returnera "magic"
m.return_value = "magic"

print(m())



def koo():
    """
    Function used to return value in a Mock
    """
    return "functional magic"

# Om side_effect är satt till en funktion som returnerar ett värdet kommer
# det värdet returneras och inte värdet från ".return_value".
m.side_effect = koo
print(m())



# side_effect kan också vara en sekvens
m.side_effect = [1, 2, 3]
# Då returneras nästa element varje gång mocken anropas.
print(m())
print(m())
print(m())
# Kastar StopIteration
# print(m())



# Kan också använda side_effect för att kasta ett exception när en metod anropas.
def raise_exception():
    """
    How to riase an exception in mocked function/method
    """
    raise ValueError()

m.chaos = raise_exception
# m.chaos()
# ValueError



# Vi kan lägga till attribut på Mock objektet också
m.something = "magic"
print(m.something)

# Låtsas skapa funktioner och bestämma vad de ska returnera
m.boo.return_value = "funcational magic"
print(m.boo())



# Vi kan göra väldigt mycket och dynamiska saker med Mock.
# Detta var grunderna i Mock, för att testa input ska vi använda oss av
# Mock.patch. Fortsätt kolla i filen patch.py.
