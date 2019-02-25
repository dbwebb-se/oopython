#!/usr/bin/env python3

"""
4f0f4303446816a357575ceb56d1fa7d
oopython
lab1
v2
anar12
2017-12-08 13:46:00
v2.3.8 (2017-10-19)

Generated 2018-02-02 09:24:30 by dbwebb lab-utility v2.3.9 (2017-12-28).
https://github.com/mosbth/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 1 - oopython
#
# If you need to peek at examples or just want to know more, take a look at
# the [Python documentation](https://docs.python.org/3/library/index.html).
# Here you will find everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Objects and classes
#
# Basic object oriented python.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a new file, for creating classes in. Create a class called Cat in
# your new file. Give the Cat class the instance attribute `eye_color` and
# `name` in the constructor. Make it so that values for the attributes can be
# sent as arguments to the constructor.
# Create a *get*-method for each attribute.
#
#
# Dont forget to import the file!
#
# In the code below initiate a new variable named `cat` with a new *Cat
# object*, give it eye color "black" and name "Denna".
#
# Answer with the string "My cats name is `name` and has `eye-color` eyes.",
# use your get-methods to retrieve the values..
#
# Write your code below and put the answer into the variable ANSWER.
#




testing!!!!

ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Expand your Cat class with the instance attribute `lives-left` and a *set*-
# and *get*-method for the attribute.
#
# Initialize the attribute in the constructor to `-1`. In the code below use
# the set-method to change the value to `9`.
#
# Answer with number of lives the cat has left.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a new method in the Cat class, called `description`. The method
# should return the string "My cats name is `name`, has `eye-color` eyes and
# `lives-left` lives left to live.".
#
# Answer with the result returned from the method.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a static attribute in the Cat class, "nr_of_paws", that contains the
# number of paws a cat have. Set its value to `4` in the declaration.
# Also create a method for the class that returns "self.nr_of_paws".
#
# Answer with the string "`Denna` has `4` paws"
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# In the code below, for your **cat variable**, assign the nr_of_paws
# attribute to `3`.
#
# Answer with the string "`Denna` has `3` paws but cats have
# `<Cat.nr_of_paws>` paws.".
# Use the method, from previous exercise, to get how many paws `Denna` have
# and the class name, "Cat.nr_of_paws", to get how many paws cats have.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# Create a new class named Dog, it should have the same attributes and
# methods as the Cat class.
# But in the description method return "My dogs name..." instead of "My cats
# name...".
#
# In the constructor set lives left to live to `1`.
#
# Dont forget to import the new class!
#
# In the code below initiate a new variable called `dog` with the *Dog
# class*. Give dog the name "Nova" and eye color "blue".
#
# Put cat and dog variables in a list. Iterate through the list and
# concatenate the result from their description methods together in a string,
# without any seperation between the two string.
#
# Answer with the string.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.7 (1 points)
#
# Create a new class named Duration.
# Declare the instance attributes `hours`, `minutes` and `seconds` in the
# constructor. Make it so that values for the attributes can be sent as
# arguments to the constructor.
# Give the class a method named `info` that returns duration as a string with
# the format "h-m-s". Numbers below 10 should have a leading zero when
# returned in the info method.
#
#
# Initialize a new *Duration object* and assign it to a variable called
# `duration1`. Give it hours `39`, minutes `6` and seconds `14`.
#
# Answer with the result from the info method.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.7", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.8 (1 points)
#
# Create a static method in your Duration class. The method should take one
# argument, a string in the format as the one `info` returns, "h-m-s", and
# return the duration it represents converted to number of seconds.
#
# Answer with the result from the new static method, use `duration1.info()`
# as argument to it.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.8", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Overriding methods
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Overload the `add operator(+)` in the Duration class.
# It should return the duration of two objects added together, in seconds.
#
# Initialize a new Duration object to a variable called `duration2` , give it
# hours `33`, minutes `26` and seconds `7`.
#
# Answer with `duration1+duration2`.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Overload the `iadd operator(+=)` in the Duration class to update the own
# object with the sum of each unit,  hours+hours, minutes+minutes and
# seconds+seconds.
#
# Initialize a new Duration object to a variable called `duration3` , give it
# hours `10`, minutes `27` and seconds `42`.
# In the code use "+=" to update `duration2` with `duration3`.
#
# Answer with `duration2`s info method.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# Overload the `smaller than operator(<)` in the Duration class.
# It should return True if the duration is shorter than the other.
#
# Answer with `duration1<duration2`.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)


dbwebb.exit_with_summary()
