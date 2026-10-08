# creating tuples
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# tuple length
print(f"Tuple length: {len(thistuple)}")

# creating tuple with one item
thistuple = ("apple",)
print(type(thistuple))

# not a tuple
thistuple = "apple"
print(type(tuple))

# creating an empty tuple
thistuple = ()
print(type(thistuple))

# a tuple can contain different data types
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

# creating tuple with tuple() constructor
thistuple = tuple(("apple", "banana", "cherry", "apple", "cherry"))
print(thistuple)
