from .views import employee_viewset
from django.urls import include, re_path


urlpatterns = [
    re_path(r"", include(employee_viewset.urls)),
]
