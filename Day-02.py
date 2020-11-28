from random import randint
from time import sleep
title = 'DESAFIO 58'
print('{:=^40}'.format(title))
print('-=-' * 15)
print('Vou pensar em um numero entre 0 e 10. Tente adivinhar...')
print('-=-' * 15)
count = 0
computador = 0
jogador = 1

while computador != jogador: 
    jogador = int(input('Em que numero eu pensei ?  '))
    computador = randint(0, 10)
    print('PROCESSANDO...')
    sleep(3)   
    if computador == jogador:
        print('PARABÉNS!! Você consegui me vencer!')
    else:
        count += 1 
        print('GANHEI!! Eu pensei no numero \033[1;34m{}\033[m e não no \033[1;31m{}\033[m!'.format(computador, jogador))
print('Você tentou \033[1;34m{}\033[m vezes até acertar, espero que consiga menos na proxima hehe!!'.format(count))