import os
import tempfile
import pytest
from app import create_app

@pytest.fixture()
def app():
    '''Instance of creating of app'''
    return create_app()
