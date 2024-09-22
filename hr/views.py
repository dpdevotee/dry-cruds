from django.urls import reverse
from django.views.generic import TemplateView
from django_filters import CharFilter, FilterSet
from django_tables2 import Table

from common.filters import DateFromToRangeFilter, RangeFilter
from common.viewset import TableViewSet

from .forms import EmployeeForm, JobForm
from .models import Employee, Job


class EmployeeTable(Table):
    class Meta:
        model = Employee
        template_name = "django_tables2/bootstrap5.html"
        fields = (
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "hire_date",
            "job",
            "salary",
            "manager",
            "department",
        )


class EmployeeFilter(FilterSet):
    first_name = CharFilter(lookup_expr="icontains", label="First name")
    last_name = CharFilter(lookup_expr="icontains", label="Last name")
    email = CharFilter(lookup_expr="icontains", label="Email")
    phone_number = CharFilter(lookup_expr="icontains", label="Phone number")
    hire_date = DateFromToRangeFilter(label="Hire date")
    salary = RangeFilter(label="Salary")
    job = CharFilter(field_name="job__job_title", lookup_expr="icontains", label="Job")
    manager = CharFilter(field_name="manager__last_name", lookup_expr="icontains", label="Manager")
    department = CharFilter(field_name="department__department_name", lookup_expr="icontains", label="Department")

    class Meta:
        model = Employee
        fields = []


employee_viewset = TableViewSet(
    model=Employee,
    table_class=EmployeeTable,
    filterset_class=EmployeeFilter,
    base_url_pattern="employees",
    base_url_name="employees",
    form_class=EmployeeForm,
)


class JobTable(Table):
    class Meta:
        model = Job
        template_name = "django_tables2/bootstrap5.html"
        fields = (
            "job_title",
            "min_salary",
            "max_salary",
        )


class JobFilter(FilterSet):
    job_title = CharFilter(lookup_expr="icontains", label="Job title")


job_viewset = TableViewSet(
    model=Job,
    table_class=JobTable,
    filterset_class=JobFilter,
    base_url_pattern="jobs",
    base_url_name="jobs",
    form_class=JobForm,
)


class HomeView(TemplateView):
    template_name = "hr/home.html"
    extra_context = {
        "links": {
            employee_viewset.list_url_name: "Employees",
            job_viewset.list_url_name: "Jobs",
        }
    }
