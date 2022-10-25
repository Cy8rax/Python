# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

data = list(map(int, input('Enter numbers separated by "space": ').split()))

print(data)

new_list = []
[new_list.append(i) for i in data if i not in new_list]

print(f'List of unique elements: {new_list}')