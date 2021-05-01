d, m, y = int(input('Enter the day: ')), int(input('Enter the month: ')), int(input('Enter the year: '))
def is_magic(d, m, y):
    if d * m == y % 100:
        return True
    return False
def all_magic():
    for y in range(1900, 2000):
        for m in range(1, 13):
            for d in range(1, 32):
                if is_magic(d, m, y):
                    print(f'{d}/{m}/{y} is a magic date.')
print(is_magic(d,m,y))
all_magic()