# function that can take any number of arguments, but can only have one expression

x = lambda x: x + 10
multiply = lambda a, b: a * b
print(x(10))
print(multiply(12, 32))


def nth_power(n):
    return lambda a: a**n


my_square = nth_power(2)
print(my_square(12))

numbers = [1, 2, 3, 4, 5]
# lambda with built in function
doubled = list(map(lambda a: a * 2, numbers))
print(doubled)
