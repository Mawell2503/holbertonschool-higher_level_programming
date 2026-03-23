import json
#  for structured data(like dictionaries)

def serialize_and_save_to_file(data, filename):
    with open(filename, "w") as file:
        #  writes a python dictionary into JSON file
        json.dump(data, file)

def load_and_deserialize(filename):
   with open(filename, "r") as file:
        #  reads a JSON file & converts it to a python dictionary
        return json.load(file)
