#!/usr/bin/env python3
import requests
import json
from pprint import pprint

URL= "http://127.0.0.1:2224/"

new_char= {
        "name": "Arya Stark",
	"gender": "Female",
	"aliases": [
    		        "Arya Horseface",
                        "Arya Underfoot",
                        "Arry",
                        "Lumpyface",
                        "Lumpyhead",
                        "Stickboy",
                        "Weasel",
                        "Nymeria",
                        "Squan",
                        "Saltb",
                        "Cat of the Canaly",
                        "Bets",
                        "The Blind Girh",
                        "The Ugly Little Girl",
                        "Mercedenl",
                        "Mercye"
	        ],
	"allegiances": [
		        "https://www.anapioficeandfire.com/api/houses/362"
                ]
        }

# json.dumps converts python object --> JSON string
new_char= json.dumps(new_char)

# requests.post req >=two arguments
# a url to send request / json string attached to request
resp= requests.post(URL, json=new_char)

# pretty-print the response back from our POST request
pprint(resp.json())