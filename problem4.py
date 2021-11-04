class Function:
    def __call__(self, value):
        raise NotImplementedError


class CompositeFunction(Function):
    def __init__(self, *functions):
        # TODO: fill this code
        # NOTE: `functions` is a tuple of arguments
        iterator = iter(functions)
        self.f1 = iterator.__next__()
        self.f2 = iterator.__next__()
        self.f3 = iterator.__next__()
        # print(self.f3(1))

    def __call__(self, value):
        # TODO: fill this code
        # HINT: `reversed(TUPLE)` returns a tuple in reversed order
        value2 = self.f1(value)
        print(value2)
        value3 = self.f2(value2)
        print(value3)
        return self.f3(value3)


class F(Function):
    def __call__(self, value):
        return value + 1


class G(Function):
    def __call__(self, value):
        return value ** 2


class H(Function):
    def __call__(self, value):
        return value - 3


if __name__ == "__main__":
    f = F()
    g = G()
    h = H()

    func = CompositeFunction(h, g, f)

    print(func(2))  # 6
