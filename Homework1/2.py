#2 Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

numbers=input('Введите последовательно числа x y z через пробел: ').split()
count=0

for i in range(3):
    for q in range(3):
        for k in range(3):
            part_one = not (int(numbers[i]) or int(numbers[q]) or int(numbers[k]))
            part_two = not int(numbers[i]) and not int(numbers[q]) and not int(numbers[k])
            if part_one == part_two:
                count=count+1
if count == 3**3:
    print('Все возможные варианты проверены, выражение истинно!')
else:
    print('Это странно, но выражение не истинно!')