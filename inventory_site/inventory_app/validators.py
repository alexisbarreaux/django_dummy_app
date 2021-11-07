import re
from datetime import date

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_GTIN(value):

    if not re.match("^[0-9]{8,14}$", value):
        raise ValidationError(
            _(
                "%(value)s is not a valid GTIN. Use only numbers and between 8 and 14 of them."
            ),
            params={"value": value},
            code="Wrong GTIN format",
        )


def validate_date_not_passed(value):
    if value < date.today:
        raise ValidationError(
            _("%(value)s you can't create a product with a passed expiry date."),
            params={"value": value},
            code="Wrong expiry dates",
        )
