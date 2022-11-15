#Создайте программу для игры с конфетами человек против человека.

import os
import random

def clear():
    os.system('clear')

def menu():
    print('''
                ___      .-""-.      ___
                \  "-.  /      \  .-"  /
                > -=.\/        \/.=- <
                > -='/\        /\'=- <
                /__.-'  \      /  '-.__\
                        '-..-'         
                    BATTLE FOR SWEETS!!!               
                        ''')
    opt = int(input('''
    Choose game mode:
        1 - 1 VS 1
        2 - 1 VS PC
        3 - Exit
    Enter your choice: 
        '''))
    clear()
    return opt

def winner(x):
    print(f'Player: "{x}" WINS the game! Congratulations!')
    exit()

def one_vs_one():
    print('Player VS Player')
    p_1 = input('Player one - enter your name: ')
    p_2 = input('Player two - enter your name: ')

    print('''
        The rules are rather simple - there are 2021 sweets before you, 
        each turn you can take no more than 28.\n
        The one who takes the last sweets - WIN!!!\n
        GOOD LUCK!!!\n''')

    sweets = 2021
    s1 = 0
    s2 = 0
    while sweets > 0:
        print(f'Sweets left: {sweets}')
        s1 = int(input(f'{p_1} takes sweets: '))
        while s1 not in range(1,29):
            s1 = int(input('Remember! From 1 to 28 only!\n'))
        sweets -= s1
        clear()
        print(f'Sweets left: {sweets}')
        if sweets <= 0:
            winner(p_1)    
        s2 = int(input(f'{p_2} takes sweets: '))
        while s2 not in range(1,29):
            s2 = int(input('Remember! From 1 to 28 only!\n'))
        sweets -= s2
        if sweets <= 0:
            winner(p_2)   
        clear()




def bot_play():
    clear()
    diff = int(input('''
        Choose difficulty:
            1 - wuss
            2 - hard ass\n
                '''))
    print('Player VS PC')
    p_1 = input('Player one - enter your name: ')
    p_2 = 'CPU'

    print('''
        The rules are rather simple - there are 2021 sweets before you, 
        each turn you can take no more than 28.\n
        The one who takes the last sweets - WIN!!!\n
        GOOD LUCK!!!\n''')    
    sweets = 2021
    s1 = 0
    s2 = 0
    sequence = random.randint(0,1)
    im_first = False
    if diff == 1:
        while sweets > 0:
            if sequence:
                s1 = int(input(f'Sweets left: {sweets}\n {p_1} takes sweets: '))
                while s1 not in range(1,29):
                    s1 = int(input('Remember! From 1 to 28 only!\n'))
                sweets -= s1
            sequence = True
            clear()
            print(f'Sweets left: {sweets}')
            if sweets <= 0:
                winner(p_1)    
            s2 = random.randint(1,29)
            print(f'{p_2} takes {s2} sweets')
            sweets -= s2
            if sweets <= 0:
                winner(p_2)   
    if diff == 2:
        while sweets > 0:
            if sequence:
                s1 = int(input(f'Sweets left: {sweets}\n {p_1} takes sweets: '))
                while s1 not in range(1,29):
                    s1 = int(input('Remember! From 1 to 28 only!\n'))
                sweets -= s1
            clear()
            print(f'Sweets left: {sweets}')
            if sweets <= 0:
                winner(p_1)  
            # Bot Brains  
            if not sequence or im_first:
                if not sequence:
                    s2 = 2021 % 29
                    im_first = True
                else:
                    s2 = 29-s1
            else:
                if s1 != 20 and sequence !=2:
                    im_first = True
                    s2 = sweets % 29
                elif im_first == False:
                    s2 = random.randint(1,29)
            print(f'{p_2} takes {s2} sweets')
            sweets -= s2
            if sweets <= 0:
                winner(p_2)
            sequence = 2


if menu() == 1:
    one_vs_one()
elif menu() == 2:
    bot_play()
else: exit()