"""
Author: Siddhant Mahajani
readData.py - Read data from the csv and remove null/na records from csv
"""

import pandas as pd


def read(location):
    data = pd.read_csv(location, header=0, sep=';')
    return data


def removenull(data):
    data = data.dropna(subset=['Income'])
    return data


def writedata(data, location):
    file = open(location, 'w')
    file.write(data)
    file.close()
