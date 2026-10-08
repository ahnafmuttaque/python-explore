thistuple = ("apple", "banana", "cherry")
# accessing an item
print(thistuple[0])

# with negative indexing
print(thistuple[-1])

# range indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# from start to specific index
print(thistuple[:4])

# from specific to the end
print(thistuple[2:])

# from start to end
print(thistuple[:])

# check if an item exists
if "apple" in thistuple:
    print(f"apple is in the tuple {thistuple}")
