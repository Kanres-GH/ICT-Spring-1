print('Celsius  |   Farenheit')
print('________/|\___________')
for i in range(0, 101, 10):         #   Цикл от 0 до 100
    f = float((i*(9/5))+32)         #   Формула перевода в Фаренгейты
    print(f"{'%3d'%i} °C   |   {f} °F")     #    Вывод f-строкой
