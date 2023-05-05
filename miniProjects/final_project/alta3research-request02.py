#!/usr/bin/env python3
"""Final MiniProject Using Flask Pt. 2 | Peak Seekers App | Caleb Wise"""

import json
import requests
import random
from pprint import pprint

url= "http://127.0.0.1:2224/alldata"  # added /data to go to the new endpoint

resp= requests.get(url).json() # oops! was missing the () at the end of the line

pprint(resp)


