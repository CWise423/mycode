#!/usr/bin/env python3
"""Final MiniProject Using Flask | Braves Fan Page | Caleb Wise"""

import json
import random
from flask import Flask, redirect, url_for, render_template, request

with open("mountains.json", "r") as peaks:
    data= json.load(peaks)

app = Flask(__name__)

# oh I see the problem
# so there is no function defined under the decorator on line 13
# so dumb ol' python is assigning two decorators to your success() function below
# and when you go to "/" by itself, you are not providing a value for <name>
# and without "name" defined, the function throws a fit
# so either delete line 13 or add a function below it- that will fix the issue you currently have

@app.route("/success/<name>")
def succes(name):
    return f"Welcome {name}\n"

@app.route("/start")
def start():
    return render_template("peakseeker.html")

def peak_from_list(liststr):
    """returns a randomly selected peak from the given mountain range"""
    while True:
        random.shuffle(data)
        for eachpeak in data:
            if liststr.lower() in eachpeak["range"].lower():
                return eachpeak

        return "Sorry, no peaks from your choice are in the top 10."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
