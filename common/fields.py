from django_filters.fields import DateRangeField as StandardDateRangeField
from django_filters.fields import RangeField as StandardRangeField

from .widgets import DateRangeWidget, RangeWidget


class DateRangeField(StandardDateRangeField):
    widget = DateRangeWidget


class RangeField(StandardRangeField):
    widget = RangeWidget
