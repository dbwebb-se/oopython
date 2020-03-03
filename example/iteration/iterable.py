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
iterable = iter(l)
print("Manuall")
print(next(iterable))
print(next(iterable))
print(next(iterable))
print(next(iterable))
# Lyfter exception
# print(next(iterable))
print("------------------")

# Detta är grunden i en for-loopar
# Vi kollar på hur en for-loop faktist fungerar



# Det skapas en evighets while-loop
print("Actuall for-loop")
iter_obj = iter(l)
while True:
    try:
        # get next item
        element = next(iter_obj)
        # do something
        print(element)
    except StopIteration:
        # StopIteration lyfts när iter_obj har slut på element
        # och då bryter vi loopen
        break


print("------------------")
# Vi kan bygga egna iteratorer/göra så att objekt av våra klasser kan itereras
# Vi behöver bara implementera __iter__() och __next__()
class Counter:
    """
    Simple example class for iterable
    Counts from 0 to max
    """
    def __init__(self, max_=0):
        self.max_ = max_
        self._count = 0
    def __iter__(self):
        self._count = 0
        return self
    def __next__(self):
        # var noga med att komma ihåg att lyfta StopIteration
        # Annars skapas en evighetsloop. Tänk rekursion, vi måste ha ett basfall
        if self._count > self.max_:
            raise StopIteration
        else:
            value = self._count
            self._count += 1
            return value

print("Egen klass med iter och next")
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



# Vi kan skapa egna iterable på ett lättare sätt, men yield genom att skapa
# generators
