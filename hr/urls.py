from django.urls import include, re_path

from .views import HomeView, employee_viewset, job_viewset

urlpatterns = [
    re_path(r"", include(employee_viewset.urls)),
    re_path(r"", include(job_viewset.urls)),
    re_path(r"", HomeView.as_view()),
]
