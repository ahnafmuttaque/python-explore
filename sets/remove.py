thisset = {"apple", "banana", "cherry"}
# removing an item from the set
# raises an error if item doesn't exist
thisset.remove("apple")
print(thisset)

# using discard method
# won't raise an error if item doesn't exist
thisset.discard("mango")
print(thisset)

# pop() remove an random item from the set
removed_item = thisset.pop()
print(removed_item)
print(thisset)

# clear() empties the set
thisset.clear()
print(thisset)

# del delete the keywords completely
del thisset
