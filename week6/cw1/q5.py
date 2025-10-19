class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print(self.width * self.height)

    def perimeter(self):
        print(2 * (self.width + self.height))


rectangle = Rectangle(4, 5)

rectangle.area()
rectangle.perimeter()