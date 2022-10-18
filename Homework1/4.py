#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

position = int(input('Введите номер четверти оси координат: '))

if position > 4 or position <1:
    print('Такой четверти не существует.')
elif position == 1:
    print('(0;x)U(0;y)')
elif position == 2:
    print('(-x;0)U(0;y)')
elif position == 3:
    print('(-x;0)U(-y;0)')
else:
    print('(0;x)U(-y;0)')