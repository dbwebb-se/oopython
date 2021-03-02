"""
Iterators finns överallt i python., for-loopar, comprehension och generatorer.
En iterator är ett objekt vi kan iterera över.
Egentligen behöver ett iterator objek implementera två metoder
__iter__() och __next__()
Om vi kan få en iterator från ett objekt kan vi kalla det iterable.

De flesta inbyggda datastrukturerna som list, tuple och string är iterable.

__iter__() ska returnera en Iterator
__next__() ska returnera nästa element från iteratorn
"""

# Vi kan använda next() för att manuellt iterera över en iterator.
# Om det inte finns fler element kommer den kasta errot StopIteration.

# Itterera en lista med for-loop
l = [0, 1, 2, 3]
print("For-loop")
for i in l:
    print(i)
print("_---------------")



# Manuell itterering med iter() och next()
# https://docs.python.org/3/library/functions.html#iter
# https://docs.python.org/3/library/functions.html#next
iterable = iter(l) # måste skapa iter från listan
print("Manuall")
print(next(iterable))
print(next(iterable))
print(next(iterable))
print(next(iterable))
# Lyfter exception
# print(next(iterable))
print("------------------")

# Vi itererar inte direkt över listan, utan ett list_iterator objekt.
print(type(iterable))
# <class 'list_iterator'>

# Detta är grunden i en for-loopar
# Vi kollar på hur en for-loop faktist fungerar



# Det skapas en evighets while-loop
print("Actuall for-loop")
iter_obj = iter(l)
while True:
    try:
        # get next item
        element = next(iter_obj)
        # our code
        print(element)
    except StopIteration:
        # StopIteration lyfts när iter_obj har slut på element
        # och då bryter vi loopen
        break


print("------------------")


# Vi kan bygga egna iteratorer/göra så att objekt av våra klasser kan itereras
# Vi behöver bara implementera __iter__() och __next__()

# Skapa en lista som är iterator
class CounterList:
    """
    Simple example class for iterable
    Counts from 0 to max
    """
    def __init__(self, max_=0):
        self.max = max_
        self._count = 0
    def __iter__(self):
        """
        Skapa en lista med alla värden som ska itereras över.
        Istället för att implementera egen __next__.
        """
        #pylint: disable=unnecessary-comprehension
        return iter([v for v in range(0, self.max)])
        # Notera att vi här skapar massa nya värden och lägger i en lista.
        # Vi genererar ny data enbart för att räkna uppåt. Tänk om vi hade
        # fyllt listan med annan större data. Då blir detta ett innefektivt sätt
        # att jobba med iteratorer.

print("Egen klass med lista och iter och next")
# Detta tar tidskomplexiteten O(2N). För loopen i __iter__ och sen loopar vi igen
# här ute.
c = CounterList(4)
i = iter(c)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# StopIteration
# print(next(i))

# Instansen är en iterator
class Counter:
    """
    Simple example class for iterable
    Counts from 0 to max
    """
    def __init__(self, max_=0):
        self.max = max_
        self._count = 0
    def __iter__(self):
        # Nollställ räknaren så ett objekt kan användas i flera loopar.
        # Annars kommer counter max och den redan använts i en loop.
        self._count = 0
        return self
    def __next__(self):
        # var noga med att komma ihåg att lyfta StopIteration
        # Annars skapas en evighetsloop. Tänk rekursion, vi måste ha ett basfall
        if self._count > self.max:
            raise StopIteration
        value = self._count
        self._count += 1
        return value
        # Här nere förskapas vi inte alla värden som i klassen ovanför.
        # Utan skapar våra iter värden först när de används.
        # Dett är mer effektivt än att förskapa alla och lägga i en lista och sen itterera.

print("Egen klass med iter och next")
# Detta har tidskomplexiteten O(n). Då koden här ute loopar tillsammans med
# koden i __next__.
c = Counter(4)
i = iter(c)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# StopIteration
# print(next(i))

print("------------------")
print("Egen klass med for-loop")
for i in Counter(4):
    print(i)



# Om ni kommer ihåg från längre upp skapar en lista en nytt objekt av klassen
# list_iterator när man försöker iterera över en lista. Så gör man också ibland för
# egen skapade klasser. Så i exemplet ovanför hade vi haft en CounterIterator klass
# som vi hade skapat i __iter__ metoden och returnerat.
# Då är __next__ metoden skapad i vår iterator klass istället.


# Vi kan skapa egna iterable på ett lättare sätt, med yield genom att skapa
# generators
