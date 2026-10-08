thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

# loop through the index number
for i in range(len(thistuple)):
    print(i, thistuple[i])

# using a while loop
i = 0
while i < len(thistuple):
    print(i, thistuple[i])
    i += 1

# join tuples
tuple1 = ("a", "b", "c")
tuple_joined = thistuple + tuple1
print(tuple_joined)

# multiply tuples
multiplied_tuple = tuple1 * 2
print(multiplied_tuple)

# tuple methods
print(f"apple in {thistuple}: {thistuple.count('apple')}")
print(f"index of apple in {thistuple}: {thistuple.index('apple')}")
