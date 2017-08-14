import os
import pprint
import csv

DATADIR = "C:\Users\Alex\Desktop\data-wrangling\les1"
DATAFILE = "beatles-diskography.csv"

'''
# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!

def parse_file(datafile):
    # We'll store each row of the CSV file as a dict inside a list called data
    data = []
    with open(datafile, "r") as f:
        keys = []
        for index, line in enumerate(f):
            if index == 0:
                # The first line of the CSV file contains the column titles
                # of the CSV file, i.e. the keys of our dicts to be returned.
                # We strip any newline characters out of the titles before
                # splitting the string (between commas) into several strings
                # to be stored in the keys list
                filteredLine = line.rstrip('\n')
                keys = filteredLine.split(',')
            elif 1 <= index <= 10:
                # For each of the next 10 lines we create a list of values
                filteredLine = line.rstrip('\n')
                values = filteredLine.split(',')
                # Create a new dict
                dict = {}
                # Add new key:value pairs to the dict
                for i in range(len(keys)):
                    dict[keys[i]] = values[i]
                # Add populated dict to our list to be returned
                data.append(dict)
    return data
'''

def parse_csv(datafile):
    data = []
    n = 0
    with open(datafile, 'rb') as sd:
        r = csv.DictReader(sd)
        # line will be a dict composed of fields from 1st line in CSV file
        for line in r:
            data.append(line)
    return data

def test():
    # a simple test of my first (commented out) implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline

if __name__ == '__main__':
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_csv(datafile)
    pprint.pprint(d)
