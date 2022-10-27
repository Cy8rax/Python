#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('Enter number: '))

list = []
for i in range(number):
    a = i+2
    while number % a == 0:
        list.append(a)
        number /= a
print(f'Multipliers of the entered number: {list}')