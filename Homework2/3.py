#Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

number = int(input('Enter number: '))

def recursio(x):
    if x<=1:
        return 1
    else:
        return float(x**recursio(1+1/(x-1)))

print(recursio(number))