class B:
    class _B:
        def __init__(self, value):
            self.value = value
    _instance = None

    # By defining the method as static method,
    # you can call the method without creating an instance of the class.
    # e.g. B.get_instance()
    @staticmethod
    def get_instance():
        if B._instance is None:
            B()
        return B._instance

    # `__getattr__` is a magic method executed when there is no member in the instance.
    # Since class B does not have `value` as its member,
    # accessing `value` of an instance B will get into this __getattr__.
    # e.g.,
    #   >> b1 = B(10)
    #   >> b1.value  # b1.value -> no attribute in B -> b1.__getattr__(value)
    def __getattr__(self, name):
        return getattr(B._instance, name)

    def __init__(self, value=0):
        # TODO: fill constructor


if __name__ == "__main__":
    b1 = B(10)
    print(b1.value)
    print(B.get_instance())
    b2 = B(20)
    print(b2.value)
    print(b1.value)
    print(B.get_instance())

    """
    Expected Output (example)

    > 10
    > <__main__.B._B object at 0x10cbcc210>
    > 20
    > 20
    > <__main__.B._B object at 0x10cbcc210>

    """
