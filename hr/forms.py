from django import forms
from .models import Employee
from django_select2 import forms as s2forms


class JobWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "job_title__icontains",
    ]


class ManagerWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "first_name__icontains",
        "last_name__icontains",
    ]


class DepartmentWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "department_name__icontains",
    ]


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            "job": JobWidget,
            "manager": ManagerWidget,
            "department": DepartmentWidget,
        }
