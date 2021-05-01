n = int(input('Enter an integer (2 or greater): '))
factor = 2
if n<2:
    print('Please enter a number, that is greater than 2.')
else:
    print(f'The prime factors of {n} are:')
while factor <= n:

    if n%factor==0:
        print(factor)       #   Если factor делится на введёное число -> выводим делитель, уменьшаем n
        n//=factor
    else:
        factor+=1           #   Если factor не делится, то увеличиваем до тех пор, пока не будет делиться