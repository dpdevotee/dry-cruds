from typing import Type
from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import re_path
from django.db import models
from .buttons import ButtonLink
from django import forms
from django_tables2 import SingleTableMixin, Table, Column, A
from django_filters import FilterSet
from django_filters.views import FilterView

PK = r"(?P<pk>\d+)"


class TableViewSet:
    def __init__(
        self,
        *,
        model: Type[models.Model],
        table_class: Type[Table],
        filterset_class: Type[FilterSet],
        form_class: Type[forms.ModelForm],
        base_url_pattern: str,
        base_url_name: str,
    ):
        self.model = model
        self.table_class = table_class
        self.filterset_class = filterset_class
        self.form_class = form_class
        self.base_url_pattern = base_url_pattern
        self.base_url_name = base_url_name

    @property
    def list_url_name(self):
        return f"{self.base_url_name}_index"

    @property
    def detail_url_name(self):
        return f"{self.base_url_name}_detail"

    @property
    def create_url_name(self):
        return f"{self.base_url_name}_create"

    @property
    def update_url_name(self):
        return f"{self.base_url_name}_update"

    @property
    def delete_url_name(self):
        return f"{self.base_url_name}_delete"

    def _build_list_url(self):
        view_set = self

        class TableWithLinks(self.table_class):
            pk = Column(verbose_name="ID", accessor="pk", orderable=False, linkify=(self.detail_url_name, (A("pk"),)))

            class Meta:
                template_name = "django_tables2/bootstrap5.html"
                sequence = ("pk", "...")

        class NewView(SingleTableMixin, FilterView):
            model = self.model
            table_class = TableWithLinks
            filterset_class = self.filterset_class
            template_name = "common/viewsets/list.html"
            paginate_by = 10
            ordering = "pk"
            header = self.model._meta.verbose_name_plural.capitalize()

            def get_links(self):
                return [
                    ButtonLink(
                        text="Create new item",
                        css_classes="btn btn-primary",
                        url_name=view_set.create_url_name,
                    ),
                ]

        return re_path(f"^{self.base_url_pattern}/$", NewView.as_view(), name=self.list_url_name)

    def _build_detail_url(self):
        view_set = self

        class DisabledForm(self.form_class):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                for field in self.fields:
                    self.fields[field].disabled = True

        class NewView(UpdateView):
            model = self.model
            form_class = DisabledForm
            template_name = "common/viewsets/detail.html"

            def get_links(self):
                return [
                    ButtonLink(
                        text="Update",
                        css_classes="btn btn-primary",
                        url_name=view_set.update_url_name,
                        pk=self.kwargs["pk"],
                    ),
                    ButtonLink(
                        text="Delete",
                        css_classes="btn btn-primary",
                        url_name=view_set.delete_url_name,
                        pk=self.kwargs["pk"],
                    ),
                    ButtonLink(
                        text="Back to list",
                        css_classes="btn btn-secondary",
                        url_name=view_set.list_url_name,
                    ),
                ]

        return re_path(f"^{self.base_url_pattern}/{PK}/$", NewView.as_view(), name=self.detail_url_name)

    def _build_create_url(self):
        view_set = self

        class NewView(CreateView):
            model = self.model
            template_name = "common/viewsets/form.html"
            form_class = self.form_class

            def get_links(self):
                return [
                    ButtonLink(text="Back to list", css_classes="btn btn-secondary", url_name=view_set.list_url_name),
                ]

        return re_path(f"^{self.base_url_pattern}/create/$", NewView.as_view(), name=self.create_url_name)

    def _build_update_url(self):
        view_set = self

        class NewView(UpdateView):
            model = self.model
            template_name = "common/viewsets/form.html"
            form_class = self.form_class

            def get_links(self):
                return [
                    ButtonLink(
                        text="Cancel",
                        css_classes="btn btn-secondary",
                        url_name=view_set.detail_url_name,
                        pk=self.kwargs["pk"],
                    ),
                ]

        return re_path(f"^{self.base_url_pattern}/{PK}/update/$", NewView.as_view(), name=self.update_url_name)

    def _build_delete_url(self):
        view_set = self
        success_url_name = f"{self.base_url_name}_index"

        class NewView(DeleteView):
            model = self.model
            template_name = "common/viewsets/confirm_delete.html"

            def get_success_url(self):
                return reverse(success_url_name)

            def get_links(self):
                return [
                    ButtonLink(
                        text="No",
                        css_classes="btn btn-secondary",
                        url_name=view_set.detail_url_name,
                        pk=self.kwargs["pk"],
                    )
                ]

        return re_path(f"^{self.base_url_pattern}/{PK}/delete/$", NewView.as_view(), name=self.delete_url_name)

    @property
    def urls(self):
        return [
            self._build_list_url(),
            self._build_detail_url(),
            self._build_create_url(),
            self._build_update_url(),
            self._build_delete_url(),
        ]
