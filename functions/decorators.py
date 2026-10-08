import functools


def change_case(func):
    # preserving original metadat of my_name
    @functools.wraps(func)
    def my_inner():
        return func().upper()

    return my_inner


def make_title(func):
    # preserving original metadat of my_name
    @functools.wraps(func)
    def my_inner():
        return func().center(20, "#")

    return my_inner


@make_title
@change_case
def my_name():
    return "ahnaf mottaki"


print(my_name())

# metadata of functions
print(my_name.__name__)
