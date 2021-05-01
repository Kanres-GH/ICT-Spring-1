from math import hypot
p = 0                                                               #   Вводим переменную Perimeter
x1 = int(input('Enter the x part of the coordinate: '))             #   Ввод начальной точки X
y1 = int(input('Enter the y part of the coordinate: '))             #   Ввод начальной точки Y

x1_ = x1                                                            # Сохраняем значения начальных точек
y1_ = y1                                                            #             на потом

flag = False                                                        #   Задаём любую переменную с True или False   (Или пока input() не будет пустым)
while flag == False:                                                #       чтобы цикл мог идти до break
    x2 = input('Enter the x part of the coordinate (blank to quit): ')  
    if x2 == "":                                                    #   Если ввода нет, то прерываем функцию
        break
    else:
        x2 = int(x2)
    y2 = input('Enter the y part of the coordinate: ')
    y2 = int(y2)
    a = hypot(x2-x1, y2-y1)                                         #   Расчёт стороны многоугольника
    p += a                                                          #   Прибавляем к значению периметра
    x1 = x2                                                         #   Делаем так, чтобы x2 превращалась в x1
    y1 = y2                                                         #   Тоже самое с y2, y1
d = hypot(x1-x1_,y1-y1_)                                            #    Расчёт последней стороны многоугольника
p+=d
print(f'The perimeter of this polygon is {p}')                      #   Вывод f-строкой