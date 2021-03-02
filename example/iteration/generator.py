"""
Nu ska vi se hur man kan skapa iterators med generators.
Typ iterators V2!

Med __iter__() och __next__() behöver vi lägga till extra kod,
spara interna tillstånd (_count) och lyfta exception.
Istället kan vi använda generators för att enkelt skapa iteratorer.

En generator är en funktion som returnerar ett objekt som vi kan iterera över.
Vi gör det genom att använda yield,
https://docs.python.org/3/reference/expressions.html?highlight=yield#yield-expressions.
En funktion kan innehålla flera yield och return.
Skillnaden på yield och return är att return avslutar en funktion medan yield pausar
funktionen, sparar alla interna tillstånd och återupptar senare exekveringen från
pausen.

Det finns två stora fördelar med generatorer, tar mindre minne och kräver mindre
kod för att ska iterators.
Om ni kommer ihåg från iterable.py där skrev jag om att Counter klassen
var mer effektiv logiskt sätt, men det kräver massa extra kod. Nu ska vi se hur
vi kan göra det med yield och ännu mindre kod.
"""

def my_generator():
    """
    Function som blir generator.
    När vi anropar funktionen kommer den typ wrappas i ett generator objekt.
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
gen = my_generator() # Här wrappas vår funktion och blir ett generator objekt.
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
        """
        Här behöver vi bara skapa __iter__ metoden.
        Det är för att yield kommer skapa ett objekt som returneras.
        Som i funktionen ovanför. my_generator() returneade ett generator objekt
        vilket kommer ske här också. Så i denna metoden lägger vi koden som ska ittereras.
        """
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
#pylint: disable=unnecessary-comprehension
print("List comprehension: ", [k for k in n])
gen = (k for k in n)
# Här har vi inte skapar någon lista med data än. Vi har bara förberett för
# att generera datan ett värde åt gången.
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

# Vi kan också se på list comprehension som att skriva följande
list_with_generated_values = list((k for k in n))
# Vi skapar ett generator objekt och gör en lista av det. list() kommer itterera
# igenom hela generatorn och lägga till alla element i ett list objekt och returnera.

# Fördelar med Generatorer
# 1. Lättare att implementera över iterators
# 2. Minnes effektiva

"""
Tänk t.ex. om vi jobbar med en jätte stor fil.
Vi kan antingen läsa upp allt innehåll och spara i minnet i en lista.
Eller så använder vi oss av en generator och läser upp en rad åt gången och
gör något med den randen innan vi går vidare till nästa.
Då slipper vi loopa igenom filens innehåll två gånger och gör det bara 1 gång.
"""
