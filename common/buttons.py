from django.urls import reverse
from django.utils.safestring import mark_safe


class ButtonLink:
    def __init__(self, text: str, css_classes: str, url_name: str, *args, **kwargs):
        self.text = text
        self.url_name = url_name
        self.css_classes = css_classes
        self.args = args
        self.kwargs = kwargs

    @property
    def url(self):
        return reverse(self.url_name, args=self.args, kwargs=self.kwargs)

    def __str__(self):
        return mark_safe(f'<a class="{self.css_classes}" href="{self.url}">' f"{self.text}" "</a>")
