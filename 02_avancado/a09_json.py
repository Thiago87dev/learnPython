import json

# ************* Convert from JSON to Python *************

someJson = '{"name":"Thiago", "age":"25","city":"Joinville"}'
jsonToPy = json.loads(someJson)
print(jsonToPy['age'])

# ************* Convert from Python to JSON *************

dictPy = {
    'name': 'Thiago',
    'age': 25,
    'city': 'Joinville',
}
pyToJson = json.dumps(dictPy)
print(pyToJson)

# Convert a Python object containing all the legal data types:
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
y = json.dumps(x, indent=4) # using indent
print(y)