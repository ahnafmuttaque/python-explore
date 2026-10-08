thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"],
}

# print all key names
for key in thisdict:
    print(f"{key} : {thisdict[key]}")

# with keys
for key in thisdict.keys():
    print(f"{key} : {thisdict[key]}")

# with values
for value in thisdict.values():
    print(value)

# with items
for key, value in thisdict.items():
    print(f"{key} : {value}")
