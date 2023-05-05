#!/usr/bin/env python3
"""Final MiniProject Using Flask | Peak Seekers App | Caleb Wise"""

import json
import requests
import random
from pprint import pprint

url= "http://127.0.0.1:2224/"

resp= requests.get(url)

pprint(resp)


