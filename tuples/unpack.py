fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green, yellow, red)

# if number of variable is less than the number of values
(green, yellow, *red) = fruits
print(green, yellow, red)

(green, *tropic, red) = fruits
print(green, tropic, red)
