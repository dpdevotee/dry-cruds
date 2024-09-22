import pytest
from django.test import Client

from .factories import EmployeeFactory, JobFactory


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def employee_factory():
    def _employee_factory(**kwargs):
        return EmployeeFactory(**kwargs)

    return _employee_factory


@pytest.fixture
def job_factory():
    def _job_factory(**kwargs):
        return JobFactory(**kwargs)

    return _job_factory
