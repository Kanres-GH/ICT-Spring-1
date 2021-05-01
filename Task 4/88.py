def isvalid(a,b,c):
    cnt = 0
    if a+b>c:
        cnt += 1
        print(f'{a} + {b} > {c}  -->  True\n')
    else:
        print(f'{a} + {b} !> {c}  -->  False\n')
    if a+c>b:
        print(f'{a} + {c} > {b}  -->  True\n')
        cnt += 1
    else:
        print(f'{a} + {c} !> {b}  -->  False\n')
    if b+c>a:
        cnt += 1
        print(f'{b} + {c} > {a}  -->  True\n')
    else:
        print(f'{b} + {c} !> {a}  -->  False\n')
    if cnt == 3:
        return True
    else:
        return False
a, b, c = int(input('Enter side a: ')), int(input('Enter side b: ')), int(input('Enter side c: '))
print(isvalid(a,b,c))