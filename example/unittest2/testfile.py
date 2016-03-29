#!/usr/bin/env python3

""" test file """

from person import Person

kenneth = Person("Kenneth Lewenhagen", "Stockholm", 32) # pylint: disable=C0103

print(kenneth.get_interests())
print("")
kenneth.add_interest("Programming")
print(kenneth.get_interests())
kenneth.add_interest("Hiking")
print(kenneth.get_interests())

print()
