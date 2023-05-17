from __future__ import annotations

from django import forms
from django.utils.translation import gettext_lazy as _

from django_email_blacklist import DisposableEmailChecker

from survey.models import Survey
from secure.input_utils import is_valid_email, is_valid_phone_number



email_checker = DisposableEmailChecker()


class EmailForm(forms.Form):
    email_address = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        email_address = cleaned_data.get('email_address')
        if not is_valid_email(email_address):
            raise forms.ValidationError(
                _("The e-mail address you provide is not valid")
            )
        if email_checker.is_disposable(email_address):
            raise forms.ValidationError(
                _("The e-mail address you provide is prohibited")
            )

class PhoneNumberForm(forms.Form):
    phone_number = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        phone_number = cleaned_data.get('phone_number')
        if not is_valid_phone_number(phone_number.replace("-", "")):
            raise forms.ValidationError(
                _("The phone number you provide is not valid")
            )


class SurveyForm(forms.ModelForm):

    class Meta:
        model = Survey
        exclude = ('rate_one', 'rate_two', 'contact',)
