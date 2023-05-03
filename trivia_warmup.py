#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import pprint

URL= "https://opentdb.com/api.php?amount=5"

def main():

    data= " "

    difficulty = input("Pick a difficulty:\n > Easy\n > Medium\n > Hard\n >")
    if difficulty:
        difficulty= f"&difficulty={difficulty}"
    else : print("Not a valid response")
    
    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()
    print(URL + difficulty)

if __name__ == "__main__":
    main()
