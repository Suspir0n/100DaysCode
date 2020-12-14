# This method return the resulted of comparison.
def numberCombination(password):
    generate_possible = createCombinationPossible()
    return passwordComparison(generate_possible, password)

# This method create a combination possible and after return a list.
def createCombinationPossible():
    generate_possible = []
    for number in range(0, 10000):
        generate_possible.append(number)
    return generate_possible

# This method make a comaparison with the password generate and the password that he forgot. 
def passwordComparison(generate_possible, password):
    for password_generated in generate_possible:
        if str(password_generated) == password:
            return True
    return False