# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

path = '/home/cy8rax/Desktop/Python/Homework5/native.txt'
data = open(path,'r')

for line in data:
    text = line
#    print(f'Native text: {text}')

count = 1
coded = ''
for i in range(len(text)-1):
    if text[i] == text[i+1]:
        count += 1
    else:
        coded = coded + str(count) + text[i]
        count = 1
if count > 1 or (text[len(text)-2] != text[-1]):
    coded = coded + str(count) + text[-1]

path1 = '/home/cy8rax/Desktop/Python/Homework5/encoded.txt'
data1 = open(path1,'w')
data1.writelines(coded)
data1.close()

#для наглядности заново открыл
path1 = '/home/cy8rax/Desktop/Python/Homework5/encoded.txt'
data1 = open(path1,'r')

for line in data1:
    en_text = line

numbers = ''
decoded = ''
for i in range(len(en_text)):
    if en_text[i].isdigit():
        numbers += en_text[i]
    else:
        decoded = decoded + (en_text[i] * int(numbers))
        numbers = ''

path2 = '/home/cy8rax/Desktop/Python/Homework5/decoded.txt'
data2 = open (path2, 'w')
data2.writelines(decoded)
data2.close()

#print(f'Decoded text: {decoded}')

