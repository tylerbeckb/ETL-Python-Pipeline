
import pandas as pd
import json
import sqlite3
import sys

df_list = []

# Extracts all data and puts it in a dataaFrame
def extract(file):
    try:
        # Checks if the file given is a json file
        if file.endswith(".json"):
            # Opens the json file
            f = open(file)
            # Loads it into a variable
            data = json.load(f)
            # Iterates through the data
            for table in data:
                # Puts data into a pandas data frame
                df = pd.DataFrame(data[table])
                df_list.append(df)
            return df_list
    except:
        pass
        
# Removes duplicated rows and empty cells from all the dataFrames
def transform(df_list):
    if df_list:
        for index in range(len(df_list)):
        # Removes any duplicated rows
            df_list[index].drop_duplicates(inplace = True)
        # Removes empty cells
            df_list[index].dropna(inplace = True)
    return df_list
    

# Loads each dataFrame into a seperate table
def load(df_list):
    if df_list:
        connection = sqlite3.connect("data.sqlite")
        for index in range(len(df_list)):
            df_list[index].to_sql(f"data{index}", connection, if_exists="replace")
        connection.close()
        
if __name__ == "__main__":
    for input in sys.argv:
        dataFrame = extract(input)
        dataFrame = transform(dataFrame)
        load(dataFrame)
