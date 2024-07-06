from common.viewset import TableViewSet
from .models import Employee
from .forms import EmployeeForm


employee_viewset = TableViewSet(
    model=Employee,
    base_url_pattern="employees",
    base_url_name="employees",
    form_class=EmployeeForm,
)
