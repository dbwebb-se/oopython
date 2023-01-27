#!/usr/bin/env python3

""" Mapping of class """
#pylint: disable=import-error
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///db/example.sqlite")
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()

class Person(Base):
    """ Person class """
    __tablename__ = "persons"

    # pylint: disable=C0103
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


    def __init__(self, name, age):
        """ init """
        self.name = name
        self.age = age


    def __str__(self):
        """ overloading str """
        return f"Name: {self.name}, Age: {self.age}"


def get_all_as_list():
    """ get table persons """
    result = []
    for row in session.query(Person):
        result.append({"name": row.name, "age": row.age})
    return result

def add_to_db(name, age):
    """ dfadf """
    person = Person(name=name, age=age)
    session.add(person)
    session.commit()
