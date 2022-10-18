#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random

N = int(input("Enter N number: "))
num_list = []

# Или можно так попробовать:
#for i in range(N*2+1):
#    if i<N:
#        num_list.append(-N+i)
#    else:
#        num_list.append(i-N) 
#print(num_list)

for i in range(-N,N):
    num_list.append(random.randint(-N,N))
print(num_list)

def multiplier(entered_N):
    result=1
    path = '/home/cy8rax/Desktop/Python/Homework2/file.txt'
    data = open(path,'r')
    for number in data:
        if int(number)>(N*2+1):
                result='Index out of range!'
                return result
        else:
            result*=num_list[int(number)] 
    return result

print(multiplier(N))
   
