from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStamped(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Survey(TimeStamped):
    name = models.CharField(_("Your name"), max_length=400)
    phone_number = models.CharField(
        _("Your phone number"), max_length=13, blank=True)
    email_address = models.EmailField(_("Your email"), blank=True)
    comment = models.TextField(_("Tell us about your experience"))
    rate_one = models.PositiveIntegerField(
        _("Rate your experience"), default=1)
    rate_two = models.PositiveIntegerField(
        _("Are you willing to recommend us? Rate us"), default=1)
    contact = models.BooleanField(
        _("Would you like us to contact you?"), default=0)
    
    class Meta:
        pass

    def __str__(self):
        return f'Survey by: {self.name}'
