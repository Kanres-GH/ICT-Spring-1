#   n = int(input())
print('        ', end='') 
for i in range(1,11):       #   Выводим ряд от 1 до 10
    print(i, end = '      ')
print()
print(' ', ' _'*35)
for i in range(1,11):   #   Выводим столбец от 1 до 10
    print('%2d' % i, end = '|    ')
    for j in range(1, 11):
      print('%2d' % (i * j), end = '     ')     #  Выводим таблицу
    print()