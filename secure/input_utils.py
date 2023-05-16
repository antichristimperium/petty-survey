from __future__ import annotations

import re

from django.http import HttpRequest
from django.forms import Form


def is_valid_email(email):
    result = False
    try:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]{3,}\.[a-zA-Z]{2,}$'
        result = re.match(pattern, email) is not None
    except TypeError:
        pass
    return result


def is_valid_phone_number(phone_number):
    pattern = r'^\d{8,}$'
    return re.match(pattern, phone_number) is not None


def find_possible_field_error(request: HttpRequest, form: Form ) -> str:
    current_form = form(request.POST or None)
    field_name = [x for x in current_form.fields.keys()][0]
    possible_message_error: str = ""
    if not current_form.is_valid():
        possible_message_error = current_form.errors.as_data().get('__all__')[0].message
    return possible_message_error, field_name
