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

Create a function that takes cat1 as an argument. If evil for cat1 is true, return 'All cats are evil!' otherwise return 'This cat is not evil!'
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

Create a new class called BankAccount. It should have the attributes balance and owner, owner should be private.
The constructor should take the name for the owner, <Andreas>, and balance should be initalized to <0.0>.

It should also have three functions, showBalance, depositMoney and withdrawMoney.
showBalance returns 'Andreas has '<currentBalance>' kr'.
depositMoney adds the amount of money sent as argument to balance
withdraw money draws the amount of moeny sent as an argument from balance

create a function where you create a new instance of the class BankAccount, that takes the owner name as argument, and returns the objects.
deposit <102.23> kr to the account and answer with the showBalance function.

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

Overload the add(+) function for the BankAccount class. It should work with the currentBalance of the account.
The function should be able to add two bank accounts together(add togehter the balance of the accounts), BankAccount + int and BankAccount 0 float.
It should return a float with 2 decimals

Initiate a new BankAccount called ba2 with the owner <Zeldah> and deposit <100.00> kr to it.
Answer with ba + ba2

Write your code below and put the answer into the variable ANSWER.
"""

ba2 = createBankAccount("Zeldah")
ba2.depositMoney(100.00)
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

Create a static variable for the Cat class. It should be an int that contains the number of paws a cat has, 4.
In the code below assign the variable for cat1 to <2>.

Answer with the string '<Misty> have <cat1.nrOfPaws> paws but cats have <Cat.nrOfpaws> paws'

Write your code below and put the answer into the variable ANSWER.
"""

cat1.nrOfPaws = 2
ANSWER = "Misty have " + str(cat1.nrOfPaws) + " paws but cats have " + str(Cat.nrOfPaws) + " paws"

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
--------------------------------------------------------------------------
Section 5. Iteration and loops

For-loops and while-loops.
"""

"""
Exercise 5.1

Create a while-loop that adds 3 to the number 19, 51 times. Answer with the
result.

Write your code below and put the answer into the variable ANSWER.
"""


# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
#print(dbwebb.assertEqual("5.1", person, False))

dbwebb.exitWithSummary()
