#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input('Введите Х: '))
y = int(input('Введите Y: '))

if x == 0 and y == 0:
    print('Нулевая координата!')
elif x>0 and y>0:
    a = 1
elif x<0 and y>0:
    a = 2
elif x<0 and y<0:
    a = 3
else:
    a = 4

print(f"X={x}; Y={y} -> {a}")