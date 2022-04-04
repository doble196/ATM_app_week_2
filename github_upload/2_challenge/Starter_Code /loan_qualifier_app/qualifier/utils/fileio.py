# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from email import header
from pathlib import Path

csvpath = Path("daily_rate_sheet.csv")
with open(csvpath) as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        print(row)
        

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    
    
    with open ("csvpath, data, header "r"") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
        return data
