class A:
    def build_floor(self):
        raise NotImplementedError

    def build_body(self):
        raise NotImplementedError

    def build_ceiling(self):
        raise NotImplementedError


class House(A):
    def build_floor(self):
        print("Build House Floor")

    def build_body(self):
        print("Build House Body")

    def build_ceiling(self):
        print("Build House Ceiling")


class Building(A):
    def build_floor(self):
        print("Build Building Floor")

    def build_body(self):
        print("Build Building Body")

    def build_ceiling(self):
        print("Build Building Ceiling")


def build(cls):
    # TODO: fill this method


if __name__ == "__main__":
    build(House)
    build(Building)

    """
    Expected Output

    > Build House Floor
    > Build House Body
    > Build House Ceiling
    > Build Building Floor
    > Build Building Body
    > Build Building Ceiling

    """
