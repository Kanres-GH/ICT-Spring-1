from math import hypot
def hypotenuse(a, b):
    c = hypot(a,b)
    return c
a = int(input('Enter cathetus a: '))
b = int(input('Enter cathetus b: '))
print(f'The hypotenuse of right triangle with cathetuses {a} and {b} is', hypotenuse(a, b))