# function with default parameters
def greeting(fname="There"):
    print(f"Hello, {fname}")


greeting()

# keyword arguments
greeting(fname="ahnaf")


# positional arguments
def my_function(animal, name, age):
    print(f"I have a {age} years old {animal} named {name}")


my_function("dog", "bittle", 2)


# positional only arguments
def position_only_func(animal, name, age, /):
    return animal, name, age


animal, name, age = position_only_func("dog", "bittle", 3)
print(animal, name, age)


# keyword only arguments
def keyword_only_func(*, animal, name, age):
    return animal, name, age


animal, name, age = keyword_only_func(animal="dog", name="bittle", age=23)
print(animal, name, age)


# combining positional only and keyword only argument
def my_func(
    a,
    b,
    c,
    /,
    *,
    e,
    f,
):
    return None


my_func(1, 2, 3, e=4, f=5)


def my_kids(*kids):
    print(f"my youngest kid is {kids[-1]}")


my_kids("ahnaf", "mottaki")


def total(*numbers):
    if not len(numbers):
        return None
    total = 0
    for x in numbers:
        total += x

    return total


print(total(132, 34, 23, 66))
print(total())


# kwargs
def my_kwargs(**kwargs):
    print(kwargs)


my_kwargs(name="ahnaf", age=23, address="kanchibari")
