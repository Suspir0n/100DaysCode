import pytest
from src.row import dequeue


# testing the happy way and sad way
def test_happy_way():
    # Removes the element from the front
    elements = [['Evandro', 19], ['Ismael', 26], ['Ana Luisa', 18], ['Alisson', 16], ['Kalill', 69], ['Julio', 80]]
    last = 5
    for c in range(0, last):
        assert dequeue(elements, last) is True
        last -= 1


def test_sad_way():
    # Remove element with empty list
    elements = []
    last = -1
    message = 'The Queue it is empty!'
    assert message, dequeue(elements, last) is False
