class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, color, side1, side2, side3):
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Method Overloading
class Square(Rectangle):
    def __init__(self, color, side):
        super().__init__(color, side, side)

    # Method Overriding
    def area(self):
        return self.length * self.length

    # Method Overwriting
    def perimeter(self):
        return 4 * self.length



# Create instances of the shape classes
circle = Circle("Red", 5)
rectangle = Rectangle("Blue", 4, 6)
triangle = Triangle("Green", 3, 4, 5)
square = Square("Yellow", 5)

# Demonstrate Method Overloading
# We have overloaded the Rectangle constructor to accept a single side for Square.
print("Area of Square:", square.area())  # Calls the overridden 'area' method in the Square class

# Demonstrate Method Overriding
# The 'area' method in the Square class overrides the one in the Rectangle class.
print("Area of Rectangle:", rectangle.area())  # Calls the overridden 'area' method in the Rectangle class

# Demonstrate Method Overwriting
# The 'perimeter' method in the Square class overwrites the one in the Rectangle class.
print("Perimeter of Square:", square.perimeter())  # Calls the overwritten 'perimeter' method in the Square class
