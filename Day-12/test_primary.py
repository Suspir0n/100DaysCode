import pytest
from PasswordCheck import verifyPasswordRule

'''testing the happy way and sad way'''  
def test_happy_way():
    '''Create a password valid'''
    password = '123456'
    passwordCheckResponse = verifyPasswordRule(password) is True
    message = 'Valid password, save with success'
    assert message, passwordCheckResponse

def test_sad_way():
    '''Create a password with more digits'''
    invalidPassword = '1234567'
    if len(invalidPassword) > 6:
        passwordCheckResponse = verifyPasswordRule(invalidPassword) is False
        message = 'Invalid password, this with more digits. The Correct is 6 digits'
        assert message, passwordCheckResponse 
    '''Create a password with fewer digits'''
    invalidPassword = '12345'
    if len(invalidPassword) < 6:
        passwordCheckResponse = verifyPasswordRule(invalidPassword) is False
        message = 'Invalid password, this with fewer digits. The Correct is 6 digits'
        assert message, passwordCheckResponse
    '''Create a password with number and letters'''
    invalidPassword = '123abc'
    if invalidPassword.isalnum():
        passwordCheckResponse = verifyPasswordRule(invalidPassword) is False
        message = 'Invalid password, The password can only consist of numbers'
        assert message, passwordCheckResponse 
