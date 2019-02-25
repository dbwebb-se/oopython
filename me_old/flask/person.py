#!/usr/bin/env python3
"""
person klass

    Förnamn
    Efternamn
    Ålder
    länk till en bild som används
    Godtyckliga metoder för att underlätta utskrift.

"""
class Person():
    """
    ett person me_objekt
    """
    def __init__(self, givenname, lastname, age, pic):
        """
        initiera Person
        """
        self.givenname = givenname
        self.lastname = lastname
        self.age = age
        self.pic = pic

    def get_givenname(self):
        """
        returnera Förnamn
        """
        return self.givenname

    def get_age(self):
        """
        returnera ålder
        """
        return self.age

    def get_lastname(self):
        """
        returnera Efternamn
        """
        return self.lastname

    def fullname(self):
        """
        returnera hela namnet
        """
        return self.givenname + self.lastname

    def description(self):
        """
        returnera en beskrivning
        """
        return "Jag heter {} {} och är {} år gammal"\
        .format(self.givenname, self.lastname, self.age)

    def picture(self):
        """
        returnera bild
        """
        return self.pic
