from typing import Type
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import re_path
from django.db import models
from .buttons import ButtonLink
from django import forms

PK = r"(?P<pk>\d+)"


class TableViewSet:
    def __init__(
        self,
        model: Type[models.Model],
        base_url_pattern: str,
        base_url_name: str,
        form_class: Type[forms.ModelForm],
    ):
        self.model = model
        self.base_url_pattern = base_url_pattern
        self.base_url_name = base_url_name
        self.form_class = form_class

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

        class NewView(ListView):
            model = self.model
            template_name = "common/viewsets/list.html"

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

        class NewView(DetailView):
            model = self.model
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
