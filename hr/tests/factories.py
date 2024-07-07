import factory
from factory.django import DjangoModelFactory

from hr.models import Country, Department, Dependent, Employee, Job, Location, Region


class RegionFactory(DjangoModelFactory):
    class Meta:
        model = Region

    region_name = factory.Faker("word")


class CountryFactory(DjangoModelFactory):
    class Meta:
        model = Country

    country_id = factory.Faker("country_code")
    country_name = factory.Faker("word")
    region = factory.SubFactory(RegionFactory)


class LocationFactory(DjangoModelFactory):
    class Meta:
        model = Location

    street_address = factory.Faker("street_address")
    postal_code = factory.Faker("postcode")
    city = factory.Faker("city")
    state_province = factory.Faker("state")
    country = factory.SubFactory(CountryFactory)


class DepartmentFactory(DjangoModelFactory):
    class Meta:
        model = Department

    department_name = factory.Faker("word")
    location = factory.SubFactory(LocationFactory)


class JobFactory(DjangoModelFactory):
    class Meta:
        model = Job

    job_title = factory.Faker("word")
    min_salary = factory.Faker("random_number", digits=5)
    max_salary = factory.Faker("random_number", digits=5)


class EmployeeFactory(DjangoModelFactory):
    class Meta:
        model = Employee

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    phone_number = factory.Faker("msisdn")
    hire_date = factory.Faker("date")
    job = factory.SubFactory(JobFactory)
    salary = factory.Faker("random_number", digits=5)
    manager = None
    department = factory.SubFactory(DepartmentFactory)


class DependentFactory(DjangoModelFactory):
    class Meta:
        model = Dependent

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    relationship = factory.Faker("word")
    employee = factory.SubFactory(EmployeeFactory)
