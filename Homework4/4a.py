import random

degree = int(input("Enter coefficient - 'c' for: 2x^c + 4x^c-1 + 5x^c-2 = 0: "))

coef=[]

coef = [random.randint(0,101) for i in range(3)]

form_w = ''
if coef[0] > 0:
    form_w = f'{coef[0]}x^{degree} + '
if coef[1] > 0 and degree > 1:
    form_w += f'{coef[1]}x^{degree-1} '
elif coef[1] > 0 and degree == 1:
    form_w += f'{coef[1]+coef[2]} '
if coef[2] > 0 and degree > 2:
    form_w += f'+ {coef[2]}x^{degree-2}'

print(f'{form_w} = 0')

with open('file_one.txt', 'w') as data:
    data.write(f'{form_w} = 0')