import pytest

from hr.models import Employee, Job


@pytest.mark.django_db
def test_employees_index_view_returns_expected_context(client, employee_factory):
    # given
    employee_factory()
    employee_factory()
    employee_factory()

    # when
    response = client.get("/employees/")

    # then
    assert response.status_code == 200
    assert "table" in response.context
    assert "view" in response.context
    assert "filter" in response.context
    assert len([row for row in response.context["table"].paginated_rows]) == 3
    links = response.context["view"].get_links()
    assert links[0].text == "Create"
    assert links[0].url == "/employees/create/"


@pytest.mark.django_db
def test_employees_index_view_finds_employee_by_email(client, employee_factory):
    # given
    employee = employee_factory(email="some.cool@gmail.com")
    employee_factory()
    employee_factory()

    # when
    response = client.get("/employees/?email=cool")

    # then
    assert response.status_code == 200
    assert "table" in response.context
    assert "view" in response.context
    assert "filter" in response.context
    rows = [row for row in response.context["table"].paginated_rows]
    assert len(rows) == 1
    assert rows[0].record.pk == employee.pk


@pytest.mark.django_db
def test_employees_detail_view_shows_employee(client, employee_factory):
    # given
    employee = employee_factory()

    # when
    response = client.get(f"/employees/{employee.pk}/")

    # then
    assert response.status_code == 200
    assert "form" in response.context
    assert "view" in response.context
    links = response.context["view"].get_links()
    assert [link.text for link in links] == ["Update", "Delete", "Back to list"]
    assert [link.url for link in links] == [
        f"/employees/{employee.pk}/update/",
        f"/employees/{employee.pk}/delete/",
        "/employees/",
    ]


@pytest.mark.django_db
def test_employees_detail_view_cannot_change_employee(client, employee_factory):
    # given
    employee = employee_factory()

    # when
    response = client.patch(f"/employees/{employee.pk}/")

    # then
    assert response.status_code == 405
    assert response["Allow"] == "GET, OPTIONS"


@pytest.mark.django_db
def test_employees_create_view_creates_employee(client, employee_factory):
    # given
    manager = employee_factory()

    # when
    response = client.post(
        "/employees/create/",
        data={
            "first_name": "Vasilii",
            "last_name": "Zadov",
            "email": "vasilii.zadov@gmail.com",
            "phone_number": "+79991234566",
            "hire_date": "2022-11-10",
            "job": manager.job.pk,
            "salary": 3010,
            "manager": manager.pk,
            "department": manager.department.pk,
        },
    )

    # then
    assert response.status_code == 302
    new_employee = Employee.objects.get(email="vasilii.zadov@gmail.com")
    assert response.url == f"/employees/{new_employee.pk}/"


@pytest.mark.django_db
def test_employees_update_view_changes_employee(client, employee_factory):
    # given
    manager = employee_factory()
    employee = employee_factory(salary=3010, manager=manager)
    new_salary = 3050

    # when
    response = client.post(
        f"/employees/{employee.pk}/update/",
        data={
            "first_name": employee.first_name,
            "last_name": employee.last_name,
            "email": employee.email,
            "phone_number": employee.phone_number,
            "hire_date": employee.hire_date,
            "job": employee.job.pk,
            "salary": new_salary,
            "manager": manager.pk,
            "department": employee.department.pk,
        },
    )

    # then
    assert response.status_code == 302
    assert response.url == f"/employees/{employee.pk}/"
    updated_employee = Employee.objects.get(pk=employee.pk)
    assert updated_employee.salary == new_salary


@pytest.mark.django_db
def test_employees_delete_view_deletes_employee(client, employee_factory):
    # given
    manager = employee_factory()
    employee = employee_factory(manager=manager)

    # when
    response = client.post(f"/employees/{employee.pk}/delete/")

    # then
    assert response.status_code == 302
    assert response.url == "/employees/"
    assert Employee.objects.filter(pk=employee.pk).count() == 0


@pytest.mark.django_db
def test_jobs_index_view_returns_expected_context(client, job_factory):
    # given
    job_factory()
    job_factory()
    job_factory()

    # when
    response = client.get("/jobs/")

    # then
    assert response.status_code == 200
    assert "table" in response.context
    assert "view" in response.context
    assert "filter" in response.context
    assert len([row for row in response.context["table"].paginated_rows]) == 3
    links = response.context["view"].get_links()
    assert links[0].text == "Create"
    assert links[0].url == "/jobs/create/"


@pytest.mark.django_db
def test_jobs_index_view_finds_job_by_title(client, job_factory):
    # given
    job = job_factory(job_title="Sewage Truck Operator")
    job_factory()
    job_factory()

    # when
    response = client.get("/jobs/?job_title=sewage")

    # then
    assert response.status_code == 200
    assert "table" in response.context
    assert "view" in response.context
    assert "filter" in response.context
    rows = [row for row in response.context["table"].paginated_rows]
    assert len(rows) == 1
    assert rows[0].record.pk == job.pk


@pytest.mark.django_db
def test_jobs_create_view_creates_job(client, job_factory):
    # when
    response = client.post(
        "/jobs/create/",
        data={
            "job_title": "Sewage Truck Operator",
            "min_salary": 2000,
            "max_salary": 5000,
        },
    )

    # then
    assert response.status_code == 302
    new_job = Job.objects.get(job_title="Sewage Truck Operator")
    assert response.url == f"/jobs/{new_job.pk}/"
