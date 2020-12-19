import pytest
from src.row import dequeue


# testing the happy way and sad way
def test_happy_way():
    # Removes the element from the front
    elements = ['Evandro', 'Ismael', 'Ana Luisa', 'Alisson', 'Kalill']
    last = 4
    assert dequeue(elements, last) is True


def test_sad_way():
    # Remove element with empty list
    elements = []
    last = -1
    message = 'The Queue it is empty!'
    assert message, dequeue(elements, last) is False
