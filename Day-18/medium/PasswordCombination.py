from random import sample

def combinationOfPassword(password):
    combination_possible = createCombinationPossible(password)
    return puttingTheCombinationOrder(combination_possible, password)

def createCombinationPossible(password):
    combination_possible = ''
    generate = [[], []]
    for c in range(65, 90):
        generate[0].append(chr(c))
    for c in range(97, 123):
        generate[1].append(chr(c))
    for possible in generate:
        for c in range(0, 25):
            if possible[c] in password:
                combination_possible += possible[c]
            if str(c) in password:
                if str(c) not in combination_possible:
                    combination_possible += str(c)
    return combination_possible

def puttingTheCombinationOrder(combination_possible, password):
    password_possible = ''
    while True:    
        transforming_list = sample(combination_possible , len(combination_possible))
        password_possible = ''.join(transforming_list)
        if password_possible == password:
            return True