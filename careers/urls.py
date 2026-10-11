from django.urls import path

from . import views

app_name = "careers"

urlpatterns = [
    path("careers/", views.careers, name="list"),
    path("careers/<slug:slug>/apply/", views.apply, name="apply"),
    path("careers/<slug:slug>/applied/", views.apply_success, name="apply_success"),
]
