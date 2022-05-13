from math import sqrt


def get_eqroots(a, b, c):
    d = b ^ 2 - 4*a*c
    if d < 0:
        raise ValueError("Following equation cannot be factoriezed")
    rootd = sqrt(d)
    x = (-b+rootd)/(2*a)
    y = (-b-rootd)/(2*a)
    return x, y


print("The eq is must be in the form of ax^2 + bx + c = 0")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
x, y = get_eqroots(a, b, c)
print(f"The roots of the above equation are {x} and {y}")
