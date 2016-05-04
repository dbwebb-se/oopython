#!/usr/bin/env python3

from flask import request
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from cars import Cars

engine = create_engine("sqlite:///db/cars.sqlite")

Session = sessionmaker(bind=engine)
session = Session()

def fixCarTable():
    carsTable = ""
    all_cars = session.query(Cars).all()
    for car in all_cars:
        carsTable += """<tr><td>{id}</td><td>{model}</td>
                    <td>{price}</td><td>{country}</td>
                    <td>{manu}</td>
                    <td><a href='?del={id}'>Ta bort</a></td>
                    </tr>""".format(id=car.id, model=car.model, price=car.price, country=car.country, manu=car.manufacturer)
    return carsTable


def removeCar(delCar):
    session.query(Cars).filter(Cars.id == delCar).delete()
    session.commit()


def showCars():
    newCar = Cars(
    model=request.form["model"],
    price=request.form["price"],
    country=request.form["country"],
    manufacturer=request.form["manufacturer"])

    session.add(newCar)
    session.commit()
