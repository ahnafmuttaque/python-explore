thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# pop -> removes an item
thisdict.pop("year")
print(thisdict)

# popitem -> removes the last inserted item
thisdict.popitem()
print(thisdict)

# with the del
del thisdict["brand"]
print(thisdict)

# deleting the dictionary completely
del thisdict

# clear the dictionary
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.clear()
print(thisdict)
