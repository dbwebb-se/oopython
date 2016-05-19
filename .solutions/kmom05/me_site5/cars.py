#!/usr/bin/env python3
""" Mapping of Car class """
from sqlalchemy import Column, Float, String, Integer
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Cars(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    model = Column(String)
    price = Column(Float)
    country = Column(String)
    manufacturer = Column(String)

    def __repr__(self):
        return "Model: {m}, Price: {p}, Country: {c}, Manufacturer: {ma}".format(m=self.model, p=self.price, c=self.country, ma=self.manufacturer)
