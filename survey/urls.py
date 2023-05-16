from __future__ import annotations

from django.urls import path

from survey import views

app_name = "survey"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "validate-email-address/",
        views.validate_email_address,
        name="validate_email_address"
    ),
    path(
        "validate-phone-number/",
        views.validate_phone_number,
        name="validate_phone_number"
    ),
]