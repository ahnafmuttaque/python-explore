thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "address": {"village": "kanchibari", "post": "dhubni bazar"},
}
# copy a dict
copy_thisdict = thisdict.copy()
print(copy_thisdict)

copy_thisdict["address"]["village"] = "Gaibandha"
print(thisdict["address"]["village"])
print(copy_thisdict["address"]["village"])

# with the dict constructor
mydict = dict(thisdict)
print(mydict["address"] is thisdict["address"])
