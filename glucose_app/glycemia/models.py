from django.db import models
from utils.models import BaseDate


class Glycemia(BaseDate):
    person = models.ForeignKey(
        "person.Person",
        on_delete=models.CASCADE,
        related_name="glycemias",
    )
    value = models.PositiveSmallIntegerField()
