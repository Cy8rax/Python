#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = input("Enter number: ")
summary = 0
for i in number:
    if i!=',':
        summary+=int(i)
print(summary)