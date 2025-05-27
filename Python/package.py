#packages
#we ran "pip install cowsay" to install the cowsay package

"""
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello," + sys.argv[1]) #This will ouput as cow is calling "hello,dileep"
#if you use cowsay.trex a godzilla will call your name.
"""

#APIs

#for more info visit pypi.org/project/requests
#docs.python.org/3/library/json.html

# We need to install requests package by using pip "pip install requests"
import json #this will output the API request in json format
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]) 

#print(json.dumps(response.json(), indent=2)) #this will output the json format into readable way

o = response.json()

for result in o["results"]:
    print(result["trackName"])