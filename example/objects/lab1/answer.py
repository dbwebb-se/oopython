#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
4ace3e9796c4ef78ad8ee8da035459b5
python
lab1
anar12
2016-03-14 13:09:02
v2.0.1x (2015-09-29)

Generated 2016-03-14 14:09:02 by dbwebb lab-utility v2.0.1x (2015-09-29).
https://github.com/mosbth/lab
"""

from Dbwebb import Dbwebb
from myClass import Cat
from myClass import Dog
from myClass import BankAccount
dbwebb = Dbwebb()
print("Ready to begin.")


"""
==========================================================================
Lab 1 - oopython

If you need to peek at examples or just want to know more, take a look at
the page: https://docs.python.org/3/library/index.html. Here you will find
everything this lab will go through and much more.
"""

"""
--------------------------------------------------------------------------
Section 1. Objects and classes

The foundation of object oriented python.
"""

"""
Exercise 1.1

Create a class called Cat in a new file.
The Cat object should have the attributes eye color and name.
Initiate a variable named cat1 with a Cat object, with eye color <blue> and name <Misty>.
Access the attributes to create the string 'My cats name is <name> and has <color> eyes.'

Write your code below and put the answer into the variable ANSWER.
"""
cat1 = Cat("Misty", "blue")
ANSWER = "My cats name is %s and has %s eyes." % (cat1.name, cat1.eyeColor)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2

Expand your Cat class with number of lives left.
Initialize the attribute in the constructor to -1. Create a Set function and set the number of lives
to <5>. Then create a Get function that returns the number of lives the cat has left.

Write your code below and put the answer into the variable ANSWER.
"""

cat1.livesLeft = 5
ANSWER = cat1.livesLeft

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3

Create a new function in the Cat class that returns the string 'My cats name is <name>, has <color> eyes and has <livesLeft> lives left to live.'

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = cat1.description()

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4

Create a new class named Dog, it should look the same as the Cat class. But in the description function
it should print 'My dogs name...' instead of 'My cats name...'
Put cat1 and dog in a list. Iterate through the list and put their discriptins in a string and answer with.

Write your code below and put the answer into the variable ANSWER.
"""

dog = Dog("Misha", "green")
animalList = [cat1, dog]
description = ""
for animal in animalList:
    description += animal.description()
ANSWER = description

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5

Create a private variable for the cat class called evil. In the constructor the variable should be set to true by default
if no argument is given. Create a function in the class that returns if the cat is evil or not.
Answer with if the cat is evil or not.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = cat1.isEvil()

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6

In the code below create a function that takes cat as an argument. If attribute evil for cat is true, return 'All cats are evil!' otherwise return 'This cat is not evil!'
Answer with the returned string.

Write your code below and put the answer into the variable ANSWER.
"""
def catsAreEvil(catr):
    if catr.isEvil():
        return "All cats are evil!"
    else:
        return "This cat is not evil!"

ANSWER = catsAreEvil(cat1)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))


"""
Exercise 1.7

Create a new class called BankAccount. It give it the attributes balance and owner. Owner should be private.
The constructor should take the name for the owner. Balance should be initalized to <0.0> in the constructor. Balance shall always have 2 decimals.

It should also have three functions, showBalance, depositMoney and withdrawMoney.
showBalance returns '<Owner> has '<Balance>' kr'.
depositMoney adds the amount of money sent as argument to balance
withdraw money draws the amount of money sent as an argument from balance

In the code below create a function, where you create a new instance of the class BankAccount, that takes the owner name as argument, and returns the objects.

Create a new variable called bankAccount1 and initialize it with the create bank account function, Name the owner <Andreas>.
Deposit <102.23> kr to the account and answer with the showBalance function.

Write your code below and put the answer into the variable ANSWER.
"""
def createBankAccount(owner):
    """
    creates and returns a bank account
    """
    return BankAccount(owner)
ba = createBankAccount("Andreas")
ba.depositMoney(102.23)

ANSWER = ba.showBalance()

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))


"""
Exercise 1.8

Overload the add(+) function for the BankAccount class. It should work with the attribute balance of the account.
The function should be able to sum the balance of two bank accounts(BankAccount + BankAccount), BankAccount + int and BankAccount + float.
It should return a float with 2 decimals

Initiate a new BankAccount called bankAccount2 with the owner <Zeldah> and withdraw <100.00> kr from it.
Answer with bankAccount1 + bankAccount2

Write your code below and put the answer into the variable ANSWER.
"""

ba2 = createBankAccount("Zeldah")
ba2.withdrawMoney(100.00)
ANSWER = ba + ba2

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.8", ANSWER, False))


"""
Exercise 1.9

Overload the iadd(+=) function for the BankAccount class. It should work with the currentBalance of the account.
The function should be able to add two bank accounts together(add togehter the balance of the accounts), BankAccount + int and BankAccount 0 float.

use += to update ba's account and answer with ba's showBalande function.

Write your code below and put the answer into the variable ANSWER.
"""
ba += ba2
ANSWER = ba.showBalance()

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.9", ANSWER, False))

"""
Exercise 1.10

If you look in iadd and add for BankAccount you should be using basically the same code in both functions. To minize code size of the class, create a private function
where you do those calculations and then call it from iadd and add.

calculate ba2 += ba + <5.20>
Answer with ba2.showBalance()

Write your code below and put the answer into the variable ANSWER.
"""
ba2 += ba + 5.20
ANSWER = ba2.showBalance()

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.10", ANSWER, False))

"""
Exercise 1.11

Create a static variable in the Cat class. It should be an int that contains the number of paws a cat has, 4.
In the code below assign the variable for cat1 to <2>.

Answer with the string '<Misty> has cat1.nrOfPaws paws but cats have Cat.nrOfpaws paws'

Write your code below and put the answer into the variable ANSWER.
"""

cat1.nrOfPaws = 2
ANSWER = "Misty has " + str(cat1.nrOfPaws) + " paws but cats has " + str(Cat.nrOfPaws) + " paws"

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.11", ANSWER, False))

"""
Exercise 1.12

Create a classmethod for the cat class. It should return 'Cats have <number of paws the cat class have> paws'
Answe with cat1's new method.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = cat1.catPaws()

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.12", ANSWER, False))

"""
Exercise 1.13

Create a new class, Animal, that will act as a parent to Cat and Dog. It shall have the attributes name and eye color.
Rewrite Dog and Cat so that they inherit from Animal. Answer with the description from cat1 and dog, seperated with space.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = cat1.description() + " " + dog.description()

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.13", ANSWER, False))

"""
Exercise 1.14

create a new function in Animal named speak, it should be abstract. Overwrite it in Dog and Cat, in dog return 'Voff' and in cat 'Meow'.
Create another function in Animal called speakTwice. It should return a string where self.speak has been called twice, with space as seperation betwee nthe two.

Answer with <dog>'s speakTwice function
Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = dog.speakTwice()

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.14", ANSWER, False))

"""
Exercise 1.15

Create a static method in Dog called interact. Its input parameter should be a class, If the class is of type Cat the string 'Chase!' should be returned otherwise
return 'Lick!'

Answer with <dog>'s interact function
Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = dog.interact(cat1)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.15", ANSWER, False))

dbwebb.exitWithSummary()
