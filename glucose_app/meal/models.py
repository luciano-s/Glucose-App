from django.utils.translation import gettext_lazy as _
from django.db import models
from utils.models import BaseDate


class Meal(BaseDate):
    class MealType(models.TextChoices):
        breakfast = ("B", _("Breakfast"))
        lunch = ("L", _("Lunch"))
        snack = ("S", _("Snack"))
        dinner = ("D", _("Dinner"))

    person = models.ForeignKey(
        "person.Person",
        on_delete=models.CASCADE,
        related_name="meals",
    )
    injection = models.OneToOneField(
        "injection.Injection",
        on_delete=models.SET_NULL,
        null=True,
    )
    cho = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name=_(
            "Grams of carbohydrate",
        ),
    )
    protein = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name=_(
            "Grams of protein",
        ),
    )
    description = models.TextField()
    type = models.CharField(max_length=1, choices=MealType.choices)
