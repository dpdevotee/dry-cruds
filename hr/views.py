from django_filters import CharFilter, FilterSet
from django_tables2 import Table

from common.filters import DateFromToRangeFilter, RangeFilter
from common.viewset import TableViewSet

from .forms import EmployeeForm
from .models import Employee


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
