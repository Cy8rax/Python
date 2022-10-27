# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
import random

degree_2 = int(input("Enter coefficient for 1st formula: 2x^c + 4x^c-1 + 5x^c-2 = 0: "))

coef_2 = []

def random_coef(coef):
    for i in range(3):
        coef.append(random.randint(0,101))
    return coef

random_coef(coef_2)

def creat_form (coef,degree):
    form_w = ''
    if coef[0] > 0:
        form_w = f'{coef[0]}x^{degree} + '
    if coef[1] > 0 and degree > 1:
        form_w += f'{coef[1]}x^{degree-1} '
    elif coef[1] > 0 and degree == 1:
        form_w += f'{coef[1]+coef[2]} '
    if coef[2] > 0 and degree > 2:
        form_w += f'+ {coef[2]}x^{degree-2}'
    return form_w

with open('file_two.txt', 'w') as data:
    data.write(f'{creat_form(coef_2, degree_2)} = 0')
