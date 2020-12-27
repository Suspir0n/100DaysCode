from time import sleep

colors = (
    '\033[7;40m',  # white
    '\033[0;30;41m',  # red
    '\033[0;30;42m',  # green
    '\033[0;30;43m',  # yellow
    '\033[0;30;44m',  # blue
    '\033[0;30;45m',  # purple
    '\033[0;30;46m',  # navy blue
    '\033[0;30;47m',  # grey
    '\033[m'  # incolor
)


def title(message, color=0):
    size = len(message) + 4
    print(colors[color], end='')
    print('~' * size)
    print(f'  {message}  ')
    print('~' * size)
    print(colors[8], end='')
    sleep(1)


def py_help(comand):
    title(f'Accessing the command manual \'{comand}\'', 6)
    print(colors[0], end='')
    help(comand)
    print(colors[8], end='')
    sleep(2)


# Main Program
comand = ''
while True:
    title('SYSTEM OF PyHELP', 1)
    comand = str(input(f'\033[m Function or Library > \033[1;32m'))
    print('\033[m')
    if comand.upper() == 'END':
        break
    else:
        py_help(comand)
title('SEE YOU LATER!', 1)