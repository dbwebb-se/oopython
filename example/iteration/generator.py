"""
Nu ska vi se hur man kan skapa iterators med generators.
Med __iter__() och __next__() behöver vi lägga till extra kod,
spara interna tillstånd (_count) och lyfta exceptuion.
Istället kan vi använda generators för att enkelt skapa iteratorer.

En generator är en funktion som returnerar ett objekt som vi kan iterera över.
Vi gör det genom att använda yield,
https://docs.python.org/3/reference/expressions.html?highlight=yield#yield-expressions.
En funktion kan innehålla flera yield och return.
Skillnaden på yield och return är att avslutar en funktion medan yield pausar
funktionen, spara alla interna tillstånd och återupptar senare exekveringen från
pausen.
"""

def my_generator():
    """
    Function that becomes a generator
    """
    counter = 0
    print("Inside generator")
    yield counter

    print("Have yielded one value")
    counter += 1
    yield counter

    print("Yielding last value")
    counter += 1
    yield counter

print("Generator manuellt med next!")
gen = my_generator()
print("Created generator")
print("-")
print(next(gen))
print("-")
print(next(gen))
print("-")
print(next(gen))
print("-")
# Raises StopIteration
# print(next(gen))



print("--------------")
print("Generator med for-loop")
for i in my_generator():
    print(i)



# Generatorer används oftast inte på det sättet som vi gjorde i my_generator
# utan hur kan vi istället använda det för våra klasser?

class Node:
    """
    Example of a Node class with a generator
    """
    def __init__(self, value=None):
        self.value = value
        self.children = {}

    def __iter__(self):
        # Loop över alla nycklar i children
        for key in self.children:
            yield key

print("--------------")
print("Generator i klass")
n = Node()
n.children = {"1": Node(1), "2": Node(2), "3": Node(3), "4": Node(4)}
# Här kan ni använda ett Node objekt i en for-loop
for k in n:
    print(k)



# Generatorer producerar bara ett värde i taget till skillnad från
# t.ex. list comprehension vilket gör dem bättre på att hantera
# stora datamängder. Vi kan visa detta med hjälp av Generator expressions
# Generator expression ser ut som list comprehensions fast vi byter ut
# [] mot ().
# Den stora skillnaden mellan dem är att list comprehension producerar
# en helt ny lista medan genergators producer ett element åt gången.
print("--------------")
print("Generator vs list comprehension")
print("List comprehension: ", [k for k in n])
gen = (k for k in n)
print("Generator expression: ", gen)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# StopIteration
# print(next(gen))

# Vi får bara ett värde när vi fråga efter det.
# Vilket vi kan utnyttja för att få till
# minneseffektiva program.


# Fördelar med Generatorer
# 1. Lättare att implementera över iterators
# 2. Minnes effektiva
