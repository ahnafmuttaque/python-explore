set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

# union() and update() methods joins all items
# union allows you to join a set with other data types like tuples or lists
# update changes the original set
set3 = set.union(set2)
print(set3)

# with |
set3 = set1 | set3
print(set3)

# intesection method , we learnt this in our high school
# intersection_update works like update
set3 = set1 & set3
set3 = set1.intersection(set3)
print(set3)

set1.intersection_update(set2)
print(set1)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
# difference method contain only the items from the first set that are not present in the other set.
set3 = set1.difference(set2)
print(set3)

# with -
set3 = set1 - set3
print(set3)

# with difference_update
set3.difference_update(set1)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
# symmetric_difference method keep only the elements that are NOT present in both sets.
set3 = set1.symmetric_difference(set2)
print(set3)

# with ^
set3 = set1 ^ set3
print(set3)

# with symmetric_difference_update
set3.symmetric_difference_update(set2)
print(set3)
