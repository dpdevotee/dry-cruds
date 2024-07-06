from django.utils.safestring import mark_safe
from django.urls import reverse


class ButtonLink:
    def __init__(self, text: str, css_classes: str, url_name: str, *args, **kwargs):
        self.text = text
        self.url_name = url_name
        self.css_classes = css_classes
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        url = reverse(self.url_name, args=self.args, kwargs=self.kwargs)
        return mark_safe(f'<a class="{self.css_classes}" href="{url}">' f"{self.text}" "</a>")
