#!/usr/bin/env python3
"""
My first Flask app
"""
# Importera relevanta moduler
from flask import Flask, render_template

import functions



app = Flask(__name__)

app.debug = True
app.config.update(
    PROPAGATE_EXCEPTIONS=True
)



# functions.add_to_db("Svenne", 67)


persons = functions.get_all_as_list()



@app.route("/")
def main():
    """ Main route """
    return render_template("index.html", persons=persons)



if __name__ == "__main__":
    app.run()
