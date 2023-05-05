#!/usr/bin/env python3
"""Final MiniProject Using Flask | Peak Seekers App | Caleb Wise"""

import json
import random
from flask import Flask, redirect, url_for, render_template, request

url= "http://127.0.0.1:2224/data"

@app.route("/results/<mountain>")
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
    return render_template("result")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224, debug=True)
