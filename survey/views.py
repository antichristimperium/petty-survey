from __future__ import annotations

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_POST

from django_htmx.http import trigger_client_event
from django_htmx.middleware import HtmxDetails

from secure.input_utils import find_possible_field_error

from survey.forms import EmailForm
from survey.forms import PhoneNumberForm
from survey.forms import SurveyForm


class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails


def response_field_validation(
    possible_message_error: str, field_name: str) -> HttpResponse:
    return trigger_client_event(
        HttpResponse(status=202),
        "loadError",
        {
            "is_there_error": len(possible_message_error) > 0,
            "field_name": f"id_{field_name}",
            "message_error": possible_message_error
        }
    )


@require_http_methods(["GET", "POST",])
def index(request: HtmxHttpRequest) -> HttpResponse:
    form = SurveyForm(request.POST or None)
    if request.htmx and request.POST:
        if form.is_valid():
            form.save()
            return trigger_client_event(
                HttpResponse(status=202),
                "saveComplete",
                {
                    "success": True
                }
            )
    return render(request, "survey/index.html", 
        {
            "form": form
        }
    )


@require_POST
def validate_email_address(request: HtmxHttpRequest) -> HttpResponse:
    possible_message_error, field_name = find_possible_field_error(
        request, EmailForm)
    return response_field_validation(possible_message_error, field_name)


@require_POST
def validate_phone_number(request: HtmxHttpRequest) -> HttpResponse:
    possible_message_error, field_name = find_possible_field_error(
        request, PhoneNumberForm)
    return response_field_validation(possible_message_error, field_name)
