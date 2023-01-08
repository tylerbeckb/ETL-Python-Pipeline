import os
import pandas as pd
import json

path = '/workspaces/ETL-Python-Pipeline/'

def extract(filename):
    try:
        # Checks if the file given is a json file
        if filename.endswith(".json"):
            # Opens the json file
            f = open(filename)
            # Loads it into a variable
            data = json.load(f)
    except:
        pass

extract('data.json')
