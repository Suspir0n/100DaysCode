print('=' * 50)
print('{:^50}'.format('PLAY IN MEGA SENNA'))
print('=' * 50)
games = int(input('How many games do you want to what I draw ? '))
game = list()
print(f'-=-=-=-=-=-= DRAWING {games} GAMES =-=-=-=-=-=-')
for i in range(0, games):
    while len(game) < 6:
        num = randint(0, 60)
        if num not in game:
            game.append(num)
    game.sort()
    sleep(1)
    print(f'Game {i + 1}: {game}')
    game.clear()
print('-=-=-=-=-=-=-= < GOOD DRAW! > =-=-=-=-=-=-')