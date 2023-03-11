from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


def validate_length(value: str) -> None:
    if len(value) > 40:
        raise ValidationError(_("Name length is too big!"))
