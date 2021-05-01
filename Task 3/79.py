from random import randint
cnt = 0
max = 0
print(max)
for i in range(1,101):      #   Выводим рандомные числа от 1 до 100
    a = randint(1,100)
    if a>max:               #   Находим максимум и считаем количество обновлений
        max = a
        cnt+=1
        print(a, '<== Update')
    else:
        print(a)
print(f'The maximum value found was {max}')
print(f'The maximum value was updated {cnt} times')