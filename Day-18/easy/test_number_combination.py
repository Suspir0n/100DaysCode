import pytest
from PasswordCombination import numberCombination

'''testing the happy way and sad way'''
def test_happy_way():
    '''Create combination possible of password'''
    password = '1978'
    assert numberCombination(password) is True

def test_sad_way():
    '''Create combination with less digits'''
    invalidPassword =  '19785'
    if len(invalidPassword) > 4:
        assert numberCombination(invalidPassword) is False
    '''Create combination with numbers'''
    invalidPassword = '197abc'
    if invalidPassword.isalnum():
        assert numberCombination(invalidPassword) is False
    
        