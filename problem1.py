class Shape:
    @staticmethod
    def create(name):
        # TODO: Fill the code here
        # NOTE: Raise `ValueError("Invalid name", name)` if there is no such shape.
        if name == "circle":
            return Circle()
        elif name == "square":
            return Square()
        elif name == "line":
            return Line()
        else:
            raise ValueError("Invalid name", name)

class Circle(Shape):
    def draw(self):
        print("a")


class Square(Shape):
    def draw(self):
        print("b")


class Line(Shape):
    def draw(self):
        print("c")


if __name__ == "__main__":
    x = Shape.create("circle")
    x.draw()
    x = Shape.create("square")
    x.draw()
    x = Shape.create("line")
    x.draw()

    # Expected Output
    # > ㅇ
    # > ㅁ
    # > ㅡ
