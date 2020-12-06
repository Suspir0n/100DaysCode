print('=' * 35)
print('{:^35}'.format('BANCO DEV'))
print('=' * 35)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor 
ced = 100
total_ced = 0
while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'Total de {total_ced} cédulas de R$ {ced:.2f}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        total_ced = 0
        if total == 1:
            break
print('=' * 35)
print('Volte sempre ao BANCO DEV! Tenha um bom dia!')