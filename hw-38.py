class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        """Multiplies this fraction by another fraction 'other'"""
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other):
        """Adds this fraction to another fraction 'other'"""
        return Fraction(self.a * other.b + other.a * self.b, self.b * other.b)

    def __sub__(self, other):
        """Subtracts another fraction 'other' from this fraction"""
        return Fraction(self.a * other.b - other.a * self.b, self.b * other.b)

    def __eq__(self, other):
        """Checks if this fraction is equal to another fraction 'other'"""
        return self.a * other.b == other.a * self.b

    def __gt__(self, other):
        """Checks if this fraction is greater than another fraction 'other'"""
        return self.a * other.b > other.a * self.b

    def __lt__(self, other):
        """Checks if this fraction is less than another fraction 'other'"""
        return self.a * other.b < other.a * self.b

    def __str__(self):
        return f'Fraction: {self.a}, {self.b}'


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
assert Fraction(2, 3) > Fraction(3, 6)  # True
assert Fraction(3, 6) > Fraction(8, 18)  # True
print('OK')
