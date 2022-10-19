#Реализуйте алгоритм перемешивания списка (без создания второго списка!).
import random

n = int(input('Enter size of the list: '))
num_list = []

for i in range(n):
    num_list.append(i+1)

print(num_list)

# Самый простой вариант:
#print(random.shuffle(num_list))


def random_lst(num_list,size):
    for i in range(int(n/2)):
        j = random.randint(int(n/2),n-1)
        num_list[i], num_list[j] = j, i
    return num_list

print(random_lst(num_list,n))