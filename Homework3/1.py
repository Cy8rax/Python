#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
import random

num_list = []

def randomizer(lst):
    for i in range(5):
        lst.append(random.randint(1,10))
    return lst

def odd_multiplier(lst):
    odd=1
    for k in range(5):
        if k % 2 != 0:
            odd *= lst[k]
    return odd

print(f"In List: {randomizer(num_list)} multiplication of odd numbers is {odd_multiplier(num_list)}")