import pytest
from QueueAndDequeue import row

def main(value):
    _row = row()
    _row.Queue(value)
    return _row 

def test_happy_way_Queue():
    value = ['Evandro', 'Ismael', 'Ana Luisa', 'Alisson', 'Kalill']
    for name in value:
        assert main(name) is True
    