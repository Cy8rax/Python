#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

number = int(input("Enter number: "))
a=1
lst=[]
lst2 = '('
counter=0

for i in range(number):
    a*=(i+1)
    lst.append(a)
print(lst)

while counter != number:
    counter+=1
    for i in range(counter):
        if i==0:
            lst2 += str(i+1)
        else:
            lst2 += '*'+str(i+1)
    lst2+=', '
lst2 = lst2[:-2] + ')'

print(lst2)