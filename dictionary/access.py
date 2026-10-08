thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"],
}
# accessing item
print(thisdict["colors"])
print(thisdict.get("colors"))

# get keys
# view of the dictionary, any change in thisdict will be reflected
print(thisdict.keys())

# get values
print(thisdict.values())

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

x = car.values()

print(x)  # before the change

car["year"] = 2020

print(x)  # after the change

# items -> each item in a dictionary, as tuples in a list.
print(thisdict.items())

# if key exists
print("brand" in thisdict)
