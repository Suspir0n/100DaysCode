import pytest
from StringReverse import stringReverse

'''testing the happy way and sad way'''
def test_happy_way():
    '''Create a string for reverse valid'''
    word = 'I am a developer'
    word_reverse = 'developer a am I'
    stringReverseSuccess = stringReverse(word) is True
    assert word_reverse, stringReverseSuccess

def test_sad_way():
    '''Create a string for reverse lower'''
    invalidWord = 'i am a developer'
    invalid_word_reverse = 'developer a am i'
    stringReverseFailure = stringReverse(invalidWord) is False
    if invalidWord == invalidWord.lower():
        assert invalid_word_reverse, stringReverseFailure
   
    '''Create a string for reverse upper'''
    invalidWord = 'I AM A DEVELOPER'
    invalid_word_reverse = 'DEVELOPER A AM I'
    stringReverseFailure = stringReverse(invalidWord) is False
    if invalidWord == invalidWord.upper():
        assert invalid_word_reverse, stringReverseFailure        