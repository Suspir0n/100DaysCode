import pytest
from src.row import queue


# testing the happy way and sad way
def test_happy_way():
    # Adding the same number of elements to the list
    elements = []
    value = [['Evandro', 19], ['Ismael', 26], ['Ana Luisa', 18], ['Alisson', 16], ['Kalill', 69], ['Julio', 80]]
    last = -1
    for name in value:
        result = queue(name, elements, last)
        last += 1
    lst = result
    print(lst)
    assert lst


def test_say_way():
    # Adding an element but number of elements in the list
    elements = ['Evandro', 'Ismael', 'Ana Luisa', 'Alisson', 'Kalill']
    value = 'Julio'
    last = 4
    message = 'The Queue it is full!'
    assert message, queue(value, elements, last) is False