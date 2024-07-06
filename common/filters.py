from django_filters import DateFromToRangeFilter as StandardDateFromToRangeFilter
from django_filters import RangeFilter as StandardRangeFilter

from .fields import RangeField, DateRangeField


class DateFromToRangeFilter(StandardDateFromToRangeFilter):
    field_class = DateRangeField


class RangeFilter(StandardRangeFilter):
    field_class = RangeField
