# Вычислить число c заданной точностью d

from decimal import *

number = Decimal(input("Enter a number with decimal point: "))

d = int(input('Enter precision (numbers after point): '))

print(round(number, d))