from time import sleep
from pygame import mixer
from row import queue, dequeue

# Attributes
elements = []
last = -1

# Part of code what to play music...
mixer.init()
mixer.music.load('beethoven.mp3')
mixer.music.play()
sleep(0.5)
print('''\033[0;32m

██████╗░░█████╗░███╗░░██╗██╗░░██╗  ░█████╗░███████╗  ░█████╗░░█████╗░███████╗███████╗███████╗███████╗
██╔══██╗██╔══██╗████╗░██║██║░██╔╝  ██╔══██╗██╔════╝  ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝
██████╦╝███████║██╔██╗██║█████═╝░  ██║░░██║█████╗░░  ██║░░╚═╝██║░░██║█████╗░░█████╗░░█████╗░░█████╗░░
██╔══██╗██╔══██║██║╚████║██╔═██╗░  ██║░░██║██╔══╝░░  ██║░░██╗██║░░██║██╔══╝░░██╔══╝░░██╔══╝░░██╔══╝░░
██████╦╝██║░░██║██║░╚███║██║░╚██╗  ╚█████╔╝██║░░░░░  ╚█████╔╝╚█████╔╝██║░░░░░██║░░░░░███████╗███████╗
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ░╚════╝░╚═╝░░░░░  ░╚════╝░░╚════╝░╚═╝░░░░░╚═╝░░░░░╚══════╝╚══════╝\033[m\n\n\n''')
print(f'\033[1;34m{"WELCOME TO THE BANK OF COFFEE":^100}\033[m')
while True:
    print('''\033[1;33m
        [ 1 ] Add six people at row of bank
        [ 2 ] Show a row
        [ 3 ] Meet a person in line\033[m
        \033[1;31m[ 4 ] Exit\033[m\n''')
    option = int(input('What option you choose: '))
    while option < 1 or option > 4:
        option = int(input('Option invalid, What option you choose: '))
    if option == 1:
        for count in range(0, 6):
            print('-' * 30)
            name = str(input('What is your name: '))
            age = int(input('How old are you: '))
            result = queue([name, age], elements, last)
            last += 1
    if option == 2:
        print('=' * 30)
        print(f'{"RESULT OF ROW":^30}')
        print('=' * 30)
        print(f'{"No.":<5}{"NAME":<15}{"AGE":^10}')
        print('-' * 30)
        for i, a in enumerate(result):
            print(f'{i + 1:<3}{a[0]:<16}{str(a[1])} years')
    if option == 3:
        if dequeue(result, last) is True:
            print('\033[1;34mCustomer successfully served\033[m')
        last -= 1
    if option == 4:
        break            

