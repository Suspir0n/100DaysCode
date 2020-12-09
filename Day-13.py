expressoes = []
expressao = str(input('Digite uma expressão: '))
for i in range(0, len(expressao)):
    expressoes.append(expressao[i])
if '(' in expressoes:
    if expressoes.count('(') == expressoes.count(')'):
        print('Está expressão é valida!')
    else:
        print('Está expressão é invalida!')