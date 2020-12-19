# This method create a dictionary of colors.
def method_color():
    colors = {
        'white': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'purple': '\033[35m',
        'navy blue': '\033[36m',
        'grey': '\033[37m'
    }
    return colors


# This method get the values and print in terminal.
def message(msg, color):
    colors = method_color()
    print(f'{colors[color]}{msg}\033[m')


message('Hello Word!!', 'green')