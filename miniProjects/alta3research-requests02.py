#!/usr/bin/env python3
"""Final MiniProject Using Flask | Braves Fan Page | Caleb Wise"""

import json
import random
from flask import Flask, redirect, url_for, render_template, request

with open("mountains.json", "r") as peaks:
    data= json.load(peaks)

app = Flask(__name__)

@app.route("/success/<name>")
def succes(name):
    return f"Welcome {name}\n"

@app.route("/")
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
