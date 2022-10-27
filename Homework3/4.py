# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = int(input("Enter number: "))
list = []

while number / 2 >= 0.5:
    if number % 2 == 0:
        list.insert(0,0)
    else:
        list.insert(0,1)
    number = number / 2
    number = int(number)

print(''.join(str(e) for e in list))