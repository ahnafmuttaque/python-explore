# change tuple using lists
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
thislist = list(thistuple)
thislist.append("banana")
thistuple = tuple(thislist)
print(thistuple)

# adding tuple to a tuple
another = ("orange",)
thistuple = thistuple + another
print(thistuple)

# removing items
thislist = list(thistuple)
del thislist[0]
thistuple = tuple(thislist)
print(thistuple)

# deleting the tuple entirely
del thistuple
