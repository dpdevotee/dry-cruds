import pytest
from django.test import Client

from .factories import EmployeeFactory


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def employee_factory():
    def _employee_factory(**kwargs):
        return EmployeeFactory(**kwargs)

    return _employee_factory
