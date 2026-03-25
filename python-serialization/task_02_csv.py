#!/usr/bin/env python3
import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        #  creating an empty list
        data = []

        #  DictReader   < turns each row into a dictionary < it is an iterator
        #  mode= 'r'    < mode read
        #  newline=''   < creates a newline after each row
        with open(csv_filename, mode='r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)

            # Convert each row into a dictionary
            for row in reader:
                data.append(row)

        # Write to JSON file
        with open("data.json", mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False