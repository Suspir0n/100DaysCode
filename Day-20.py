from time import sleep

def line():
    print('-=' * 20)

def bigger(*num):
    line()
    print(f'Analizing the values passed...')
    for c in num:
        print(f'{c} ', end = '', flush = True)
        sleep(0.3)
    print(f'Were informed {len(num)} values to the all.')
    if len(num) == 0:
        print(f'The bigger value information is 0.')
    else:
        print(f'The bigger value information is {max(num)}')
    
bigger(2, 9, 4, 5, 7, 1)
bigger(4, 7, 0)
bigger(1, 2)
bigger(6)
bigger()