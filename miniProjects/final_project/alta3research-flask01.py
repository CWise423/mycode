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
            return redirect(url_for("peak_from_list", mountain=answer ))
        elif answer == "Eastern Great Smoky Mountains":
            return redirect(url_for("peak_from_list", mountain=answer ))
        elif answer == "Roan-Unaka Mountains":
            return redirect(url_for("peak_from_list", mountain=answer ))
    else : f"Sorry, there are no peaks from that range in this list."

@app.route("/results/<mountain>", methods= ["POST","GET"])
def peak_from_list(mountain):
    """returns the mountains in the given mountain range"""
    # we will need to loop over all the keys in your dictionary,
    # then check that key's value to see if the "range" is a match.
    # first we'll make an empty list:
    matches= []

    for x in data: # returns each "Mount"
        # check if the selected mountain is that location's "range"
        if mountain in data[x]["Range"]:
           # if so, add that key to the list
           matches.append(x)

    # return the list of peaks
    return render_template("results.html", matches = mountain)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224, debug=True)
