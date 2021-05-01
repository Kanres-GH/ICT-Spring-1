def median(a, b, c):
    if ((a < b and b < c) or (c < b and b < a)) :
        return b
    if ((b < a and a < c) or (c < a and a < b)) :
        return a
    else :
        return c
a, b, c = int(input('Enter 1st number: ')), int(input('Enter 2nd number: ')), int(input('Enter 3rd number: '))
print('The median of three numbers is', median(a,b,c))