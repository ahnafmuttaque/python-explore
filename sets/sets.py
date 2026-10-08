thisset = {"apple", "banana", "cherry"}
print(thisset)
print(type(thisset))

# the values in set True and 1, False and 0, are considered the same values and are treated as duplicated
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
thisset = {"apple", "banana", "cherry", False, 0, 2}
print(thisset)

# length of a set
print(len(thisset))
