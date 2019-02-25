from coin import Coin

coin1 = Coin(1)
coin5 = Coin(5)
coin10 = Coin(10)

coin5 += coin10
coin5 = coin5.__iadd__(coin10)
print(coin5.value)















# from coin import Dog

# d1 = Dog("Zimba")
# d2 = Dog("Buster")
# d3 = Dog("Olga")
# print(d1.counter)
# print(d2.counter)
# print(d3.counter)
# print(Dog.counter)
# d1.bark()
# Dog.bark()

# coin1 = Coin()
# coin1.toss()
# print(coin1.sideup)
# coin1.toss()
# print(coin1.sideup)
#
# coin2 = Coin()
# print(coin2.sideup)
# coin2.toss()
# print(coin2.sideup)
