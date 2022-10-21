# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import random
import math 

size = int(input("Enter list size: "))
list = []
result_list = []
for i in range(size):
    list.append(random.randint(1,10))

print(list)

for k in range(int(math.ceil(size/2))):
    result_list.append(list[k]*list[-k-1])

print(result_list)