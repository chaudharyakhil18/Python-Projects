class Fraction:

    def __init__(self, n, d):
        self.num = n
        self.den = d

    def __str__(self):
        # return f"{self.num}/{self.den}"
        return "{}/{}".format(self.num, self.den)

    def __add__(self, other):
        temp_num = self.num * other.den + self.den * other.num      # Cross multiply
        temp_den = self.den * other.den                             # Denominator multiplication
        return f"{temp_num}/{temp_den}"

    def __sub__(self, other):
        temp_num = self.num * other.den - self.den * other.num
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num, temp_den)

    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num, temp_den)

    def __truediv__(self, other):
        temp_num = self.num * other.den
        temp_den = self.den * other.num
        return "{}/{}".format(temp_num, temp_den)

x = Fraction(4, 5)
print("Fraction1 =",x)            # __str magic method is automatically called

y = Fraction(5, 8)
print("Fraction2",y)            # __str__ magic method is automatically called

print("Sum =",x + y)        # __add__ magic method is automatically called
print("Diff =",x - y)        # __sub__ magic method is automatically called

print("Multiply =",x * y)        # __mul__ magic method is automatically called
print("Division =",x / y)        # __truediv__ magic method is called