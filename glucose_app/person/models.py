from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from person.model_validator import validate_length


class Person(models.Model):
    class Sex(models.TextChoices):
        male = ("M", _("Male"))
        female = ("F", _("Female"))

    class DiabetesType(models.TextChoices):
        pre_diabetes = ("P", _("Pre diabetes"))
        type_1 = ("1", _("Diabetes type 1"))
        type_2 = ("2", _("Diabetes type 2"))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.TextField(validators=[validate_length])
    last_name = models.TextField(validators=[validate_length])
    sex = models.CharField(max_length=1, choices=Sex.choices)
    fast_acting_insulin = models.TextField()
    long_acting_insulin = models.TextField()
    is_carb_counting = models.BooleanField(default=False)
    breakfast_count = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=True,
    )
    lunch_count = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=True,
    )
    snack_count = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=True,
    )
    dinner_count = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=True,
    )
    breakfast_dosage = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=True,
    )
    lunch_dosage = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=True,
    )
    snack_dosage = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=True,
    )
    dinner_dosage = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=True,
    )
    correction_factor = models.PositiveSmallIntegerField(default=35)
    min_glycemia = models.PositiveSmallIntegerField(default=80)
    max_glycemia = models.PositiveSmallIntegerField(default=95)
    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    diabetes_type = models.CharField(
        max_length=1,
        choices=DiabetesType.choices,
        default=DiabetesType.type_1,
    )
