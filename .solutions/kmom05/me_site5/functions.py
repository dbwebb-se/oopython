#!/usr/bin/env python3

import json
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

def search_json(find_me):
    result = ""

    with open("static/animals.json") as animals:
        data = json.load(animals)

    result = """<table class='table'><thead><tr>
    <th>#</th>
    <th>Species</th>
    <th>Nr of legs</th>
    <th>Habitat</th></tr></thead><tbody>"""

    for key in data["animals"]:

        habitats = []
        for val in key["habitat"]:
            habitats.append(val.lower())

        if find_me.lower() in key["species"].lower() or find_me.lower() in habitats or find_me == key["legs"]:

            animal_id = key["id"]
            sp = key["species"]
            leg = key["legs"]
            ha = "<br>".join(key["habitat"])

            result += "<tr><td>{id}</td><td>{sp}</td><td>{leg}</td><td>{ha}</td></tr>".format(id=animal_id, sp=sp, leg=leg, ha=ha)

    result += "</tbody></table>"

    return result
