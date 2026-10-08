thisset = {"apple", "banana", "cherry"}
# adding one item
thisset.add("mango")
print(thisset)

# adding another sets item to current set
# works with any iterable
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
