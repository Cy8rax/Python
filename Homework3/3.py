# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
from decimal import *
getcontext().prec = 1

list = [1.1, 1.2, 3.1, 5, 10.01]
min = 0
max = 0

for i in range(len(list)):
    if list[i]- int(list[i]) < min:
        min = Decimal(list[i]) % 1
    elif list[i]- int(list[i]) > max:
        max = Decimal(list[i]) % 1    

differ = max - min

print(differ)