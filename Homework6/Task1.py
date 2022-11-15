#Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

expr = '5*5+(63*2)+2+(10*(22-5))'
#expr = '14+2*(22/11)+4/5+1+1/2'
#expr = '56+73/25*3'

number = ''
list = []
working_num = 0
for i in range(len(expr)):         #Все выражение превратил в список
    if expr[i].isdigit():
      number += expr[i]
      if i == len(expr)-1:
        list.append(float(number))
    else:
      if number != '': list.append(float(number))
      list.append(expr[i])
      number = ''

def calc(list, working_num, open_brackets, close_brackets):
  for i in range(open_brackets, close_brackets):
    if list[i] == '/':
      working_num = list[i-1] / list[i+1]
      list.pop(i+1)
      list[i] = working_num
      list.pop(i-1)
      close_brackets -= 1
      return list, working_num
    elif list[i] == '*':
      working_num = list[i-1] * list[i+1]
      list.pop(i+1)
      list[i] = working_num
      list.pop(i-1)
      close_brackets -= 1
      return list, working_num

  for i in range(open_brackets, close_brackets):
    if list[i] == '+':
      working_num = list[i-1] + list[i+1]
      list.pop(i+1)
      list[i] = working_num
      list.pop(i-1)
      close_brackets -= 1
      return list, working_num
    elif list[i] == '-':
      working_num = list[i-1] - list[i+1]
      list.pop(i+1)
      list[i] = working_num
      list.pop(i-1)
      close_brackets -= 1
      return list, working_num
  
i = 0
open_b = False
while '(' in list:    #Этот цикл для выражений со скобками

    if list[i] == '(' and open_b == False:
        open_b = True
        open_breakets = i
    elif list[i] == '(' and open_b == True:
        open_breakets = i
    elif list[i] == ')' and open_b == True:
        open_b = False
        close_breakets = i
        calc(list, working_num, open_breakets, close_breakets)
        list.pop(open_breakets)
        list.pop(open_breakets+1)
        i = 0
    i += 1
while len(list) > 2:
  open_breakets = 0
  close_breakets = len(list)
  calc(list,working_num, open_breakets, close_breakets)

print(list)