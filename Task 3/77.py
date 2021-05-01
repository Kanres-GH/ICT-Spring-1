#   print(int(input(), 2))

b = input('Input a binary number: ')
d = 0
for i in b:
    d = d*2 + int(i)
print(f'A decimal of {b} is {d}.')