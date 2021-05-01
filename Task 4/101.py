def min_frac():
    a, b = int(input('Enter the numerator: ')), int(input('Enter the denominator: '))
    d = min(a,b)
    while a%d!=0 or b%d!=0:
        d-=1
    print(f'{a}/{b} = {a//d}/{b//d}')
min_frac()