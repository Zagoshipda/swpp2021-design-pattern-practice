class Dog:
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof!"


class Person:
    def __init__(self):
        self.name = "Human"

    def talk(self):
        return "talk"


class Adapter:
    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        # `__dict__` saves the attributes of an instance in dict data type.
        # You can save additional attributes in `__dict__` by updating the dictionary.
        # e.g.,
        # >> dog = Dog()
        # >> print(dog.__dict__)
        #
        # >  {'name': 'Dog'}
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)


if __name__ == "__main__":
    dog = Dog()
    talkable = Adapter(dog, talk=dog.bark)
    print(talkable.name)
    print(talkable.talk())
