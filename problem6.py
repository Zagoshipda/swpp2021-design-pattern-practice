def args_printer(func):
    # TODO: fill this code
    # Use `print("func:", func.__name__, "args:", args, "kwargs:", kwargs)` to print arguments.
    def wrapper(*args, **kwargs):
        print("func:", func.__name__, "args:", args, "kwargs:", kwargs)
        return func(*args, **kwargs)
    return wrapper


@args_printer
def func1(x, y):
    # do something
    pass


@args_printer
def func2(x, y, keyword="something"):
    # do something
    pass


if __name__ == "__main__":
    func1(1, 3)
    func2("hello", "world", keyword="swpp")

    """
    Expected Output

    > func: func1 args: (1, 3) kwargs: {}
    > func: func2 args: ('hello', 'world') kwargs: {'keyword': 'swpp'}

    """
