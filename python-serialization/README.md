J- Java
S- Script
O- Object
N- Notation

standard format for data exchange

# JSON Function
json.dump()
Python -> JSON file     #saves python data into a .json file
e.g/
    data = {"name": "John", "age": 25}

    with open("data.json", "w") as file:
    json.dump(data, file)       < dump into a file


json.dumps()
Python -> JSON string(NOT a file)
e.g/
    data = {"name": "John", "age": 25}

    json_string = json.dumps(data)      <dumps string
    print(json_string)          

json.load()
JSON file -> Python     #reads and converts a .json file into a python dictionary
e.g/
    with open("data.json", "r") as file:
        data = json.load(file)  < read from a file

    print(data)


json.loads()
JSON string -> Python
e.g/
    json_string = '{"name": "John", "age": 25}'

    data = json.loads(json_string)
    print(data)                 < load string


