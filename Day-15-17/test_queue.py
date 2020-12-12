import pytest
from QueueAndDequeue import Queue

'''testing the happy way and sad way'''
def test_happy_way_Queue():
    '''Adding the same number of elements to the list'''
    elements = ['', '', '', '', '']
    value = ['Evandro', 'Ismael', 'Ana Luisa', 'Alisson', 'Kalill']
    last = -1
    for name in value:
        assert Queue(name, elements, last) is True
        last += 1
        
def test_say_way():
    '''Adding an element but number of elements in the list'''
    elements = ['Evandro', 'Ismael', 'Ana Luisa', 'Alisson', 'Kalill']
    value = 'Julio'
    last = 4
    message = 'The Queue it is full!'
    assert message, Queue(value, elements, last) is False
    