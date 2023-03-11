from django.utils.translation import gettext_lazy as _
from django.db import models
from utils.models import BaseDate


class Injection(BaseDate):
    class InjectionChoices(models.TextChoices):
        fast_acting = ("F", _("Fast acting"))
        long_acting = ("L", _("Long acting"))

    person = models.ForeignKey(
        "person.Person",
        on_delete=models.CASCADE,
        related_name="injections",
    )
    ui = models.DecimalField(max_digits=3, decimal_places=1)
    type = models.CharField(max_length=1, choices=InjectionChoices.choices)
