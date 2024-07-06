from django.urls import include, re_path

from .views import employee_viewset

urlpatterns = [
    re_path(r"", include(employee_viewset.urls)),
]
