from django.forms import TextInput
from django_filters.widgets import SuffixedMultiWidget


class RangeWidget(SuffixedMultiWidget):
    template_name = "common/widgets/range.html"
    suffixes = ["min", "max"]
    use_fieldset = False

    def __init__(self, attrs=None):
        widgets = (TextInput, TextInput)
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.start, value.stop]
        return [None, None]


class DateRangeWidget(SuffixedMultiWidget):
    template_name = "common/widgets/date_range.html"
    suffixes = ["after", "before"]
    use_fieldset = False

    def __init__(self, attrs=None):
        widgets = (TextInput, TextInput)
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.start, value.stop]
        return [None, None]
