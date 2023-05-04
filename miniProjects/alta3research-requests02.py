#!/usr/bin/env python3
"""Final MiniProject Using Flask | Peak Seekers App | Caleb Wise"""

import json
import random
from flask import Flask, redirect, url_for, render_template, request

with open("mountains.json", "r") as peaks:
    data= json.load(peaks)

app = Flask(__name__)

@app.route("/")
@app.route("/start")
def start():
    return render_template("peakseeker.html")

@app.route("/search", methods= ["POST"])
def search():
    if request.form.get("range"):
        answer = request.form.get("range")
        if answer == "Central Great Smoky Mountains":
            return redirect("/results")
        elif answer == "Eastern Great Smoky Mountains":
            return redirect("/results")
        elif answer == "Roan-Unaka Mountains":
            return redirect("/results")
    else : f"Sorry, there are no peaks from that range in this list."

@app.route("/results")
def peak_from_list(data):
    """returns the mountains in the the given mountain range"""
    while True:
        random.shuffle(data)
        for eachpeak in data:
            if liststr.lower() in eachpeak["range"].lower():
                return eachpeak

        return "Sorry, no peaks from your choice are in the top 10."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224, debug=True)
