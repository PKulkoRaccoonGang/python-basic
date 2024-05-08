class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.sqrt_half = 0.5

    def get_square(self):
        """Calculate the square of the rectangle"""
        return self.width * self.height

    def __eq__(self, other):
        """Check if two rectangles have the same area"""
        return self.get_square() == other.get_square()

    def __add__(self, other):
        """Add two rectangles to create a new rectangle"""
        total_area = self.get_square() + other.get_square()
        new_width = (total_area / self.height) ** self.sqrt_half
        new_height = total_area / new_width
        return Rectangle(new_width, new_height)

    def __mul__(self, n):
        """Multiply the area of the rectangle by a scalar"""
        new_square = self.get_square() * n
        new_width = (new_square / self.height) ** self.sqrt_half
        new_height = new_square / new_width
        return Rectangle(new_width, new_height)

    def __str__(self):
        return f'Rectangle: width={self.width}, height={self.height}'


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
print('Ok')
