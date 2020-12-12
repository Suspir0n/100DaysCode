# This method put the words together
def formTheStringAgain(reverse):
    new_word = ''
    for say in reverse:
        new_word += say + ' '
    return new_word

# This method reverse the sentence, placing it in decreasing order
def reverseStringDecreasingOrder(word):
    reverse = word.split()
    reverse.sort(reverse = True)
    formTheStringAgain(reverse)
    return reverse

# This is the method main, where I take all the data and return true or false
def stringReverse(word):
    reverse = reverseStringDecreasingOrder(word)
    result = formTheStringAgain(reverse)
    verifyStringReverse((word != word.upper() and word != word.lower()), result)

# This is the method where I verify if the string it is correct
def verifyStringReverse(condition, result):
    if condition is True:
        return result is True
    else:
        return result is False
    
    

