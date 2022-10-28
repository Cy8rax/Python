# Создайте программу для игры в ""Крестики-нолики"".

import os
import random

def clear():
    os.system('clear')

row1 = ['1  -  |','  -  |','  -  ']
row2 = ['2  -  |','  -  |','  -  ']
row3 = ['3  -  |','  -  |','  -  ']

end_g = False

print('WELCOME TO TIC-TAC-TOE!!! (Unlimited)        v0.8')
logo = (f'''

   1     2     3
      |     |     
{''.join(row1)}
 _____|_____|_____
      |     |     
{''.join(row2)}
 _____|_____|_____
      |     |     
{''.join(row3)}
      |     |     
      ''')
print(logo)
p_1 = input('Player one - enter your name: ')
p_2 = input('Player two - enter your name: ')
clear()

def coord_checker(a,b,tic):
    if a == 1:
        if '-' in row1[b-1]:
            row1[b-1] = row1[b-1].replace('-',tic)
            return row1
    if a == 2:
        if '-' in row2[b-1]:
            row2[b-1] = row2[b-1].replace('-',tic)
            return row2
    if a == 3:
        if '-' in row3[b-1]:
            row3[b-1] = row3[b-1].replace('-',tic)
            return row3

def table():
    print(f'''

       1     2     3
          |     |     
    {''.join(row1)}
     _____|_____|_____
          |     |     
    {''.join(row2)}
     _____|_____|_____
          |     |     
    {''.join(row3)}
          |     |     
        ''')

def checker(mark, playa):
    winner = (f'Congratulations!!! The Winner is {playa}!!!')
    if (''.join(row1)).count(mark) == 3:
        print(winner)
        exit()
    if (''.join(row2)).count(mark) == 3:
        print(winner)
        exit()
    if (''.join(row3)).count(mark) == 3:
        print(winner)
        exit()
    if mark in row1[0] and mark in row2[1] and mark in row3[2]:
        print(winner)
        exit()
    if mark in row1[2] and mark in row2[1] and mark in row3[0]:
        print(winner)
        exit()
    for i in range(len(row1)):
        if mark in row1[i] and mark in row2[i] and mark in row3[i]:
            print(winner)
            exit()            

table()
if random.randint(0,1):
    tic = 'X'
    tac = 'O'
    toe = True
    print(f'{p_1} first turn!')
else:
    tic = 'O'
    tac = 'X'
    toe = False
    print(f'{p_2} first turn!')
        
while not end_g:
    if toe:
        a,b = list(map(int, input(f'{p_1} -> Enter coordinates separated by "space": ').split()))
        coord_checker(a,b,tic)
        table()
        toe = False
        checker(tic, p_1)
    elif not toe:
        a,b = list(map(int, input(f'{p_2} -> Enter coordinates separated by "space": ').split()))
        coord_checker(a,b,tac)
        table()
        toe = True
        checker(tac, p_2)