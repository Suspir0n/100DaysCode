pt = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
dec = pt + (10 - 1) * rz
ar = pt
while pt != dec + rz:
    if pt == dec:
        ar = int(input('\nQuer ver mas quantos termos ? '))
        if ar != 0:
            dec = pt + (ar - 1) * rz
    if pt == ar:
        print('{} '.format(ar), end='-> ')
    else:    
        print('{} '.format(pt), end='-> ')    
    pt = pt + rz
print('ACABOU') 