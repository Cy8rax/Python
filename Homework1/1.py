#1 Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

day = int(input("Введите день недели: "))
if day == 6 or day == 7:
    print(f"{day} день недели - выходной")
elif day >=11:
    print(f"{day} день недели - рабочий")
else:
    print(f"{day}-такого дня не существует")