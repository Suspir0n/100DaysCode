import pytest
from PasswordCombination import combinationOfPassword

'''testing the happy way and sad way'''
def test_happy_way():
    '''Create a combination possible of password'''
    password = 'Pulin16'
    assert combinationOfPassword(password) is True
    
"""def test_sad_way():
    '''Create combination no special characters'''
    invalidPassword =  'João16'
    assert combinationOfPassword(invalidPassword) is False"""