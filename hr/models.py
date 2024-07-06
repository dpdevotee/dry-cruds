from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Region(models.Model):
    region_id = models.BigAutoField(primary_key=True, verbose_name=_("Unique ID"))
    region_name = models.CharField(verbose_name=_("Region name"), max_length=25)

    def __str__(self):
        return self.region_name


class Country(models.Model):
    country_id = models.CharField(verbose_name=_("Unique ID"), max_length=2, primary_key=True)
    country_name = models.CharField(verbose_name=_("Country name"), max_length=40)
    region = models.ForeignKey("Region", on_delete=models.CASCADE)

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name_plural = _("Countries")


class Location(models.Model):
    location_id = models.BigAutoField(verbose_name=_("Unique ID"), primary_key=True)
    street_address = models.CharField(verbose_name=_("Street address"), null=True, max_length=40)
    postal_code = models.CharField(verbose_name=_("Postal code"), null=True, max_length=12)
    city = models.CharField(verbose_name=_("City"), max_length=30)
    state_province = models.CharField(verbose_name=_("State province"), null=True, max_length=25)
    country = models.ForeignKey("Country", on_delete=models.CASCADE)

    def __str__(self):
        return self.city


class Department(models.Model):
    department_id = models.BigAutoField(verbose_name=_("Unique ID"), primary_key=True)
    department_name = models.CharField(verbose_name=_("Department name"), max_length=30)
    location = models.ForeignKey("Location", on_delete=models.CASCADE)

    def __str__(self):
        return self.department_name


class Job(models.Model):
    job_id = models.BigAutoField(verbose_name=_("Unique ID"), primary_key=True)
    job_title = models.CharField(verbose_name=_("Job title"), max_length=35)
    min_salary = models.DecimalField(verbose_name=_("Minimal salary"), max_digits=8, decimal_places=2)
    max_salary = models.DecimalField(verbose_name=_("Maximal salary"), max_digits=8, decimal_places=2)

    def __str__(self):
        return self.job_title


class Employee(models.Model):
    employee_id = models.BigAutoField(verbose_name=_("Unique ID"), primary_key=True)
    first_name = models.CharField(verbose_name=_("First name"), max_length=20)
    last_name = models.CharField(verbose_name=_("Last name"), max_length=25)
    email = models.CharField(verbose_name=_("E-mail"), max_length=100)
    phone_number = models.CharField(verbose_name=_("Phone number"), null=True, max_length=20)
    hire_date = models.DateField(verbose_name=_("Hire date"))
    job = models.ForeignKey("Job", on_delete=models.CASCADE)
    salary = models.DecimalField(verbose_name=_("Salary"), max_digits=8, decimal_places=2)
    manager = models.ForeignKey("Employee", null=True, on_delete=models.CASCADE)
    department = models.ForeignKey("Department", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("employees_detail", args=(self.pk,))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Dependent(models.Model):
    dependent_id = models.BigAutoField(verbose_name=_("Unique ID"), primary_key=True)
    first_name = models.CharField(verbose_name=_("First name"), max_length=50)
    last_name = models.CharField(verbose_name=_("Last name"), max_length=50)
    relationship = models.CharField(verbose_name=_("Relationship"), max_length=25)
    employee = models.ForeignKey("Employee", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
