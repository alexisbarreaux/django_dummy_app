from django import forms
from datetime import date

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .validators import validate_GTIN
from .models import Product


class EmployeeLoginForm(forms.Form):
    """Form for employees to log in."""

    firstname: str = forms.CharField(label="Firstname", max_length=40)
    lastname: str = forms.CharField(label="Lastname", max_length=40)


class ExpiryDateAddingForm(forms.Form):
    """Form for employees when a product was added in stock."""

    GTIN: str = forms.CharField(
        label="GTIN",
        max_length=14,
        widget=forms.TextInput(attrs={"placeholder": "Remember, 14 digits at most"}),
        validators=[validate_GTIN],
    )
    expiry_date: date = forms.DateField(
        initial=date.today(), label="Product expiry date"
    )
    product_name: str = forms.CharField(
        label="Product name (optional)",
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Only used when adding new products."},
        ),
    )

    # Overiding clean method to check that if a GTIN is new we should
    # have a non empty and valid name field.
    def clean(self):
        cleaned_data = super().clean()
        GTIN = cleaned_data.get("GTIN")
        product_name = cleaned_data.get("product_name")

        if Product.objects.filter(GTIN=GTIN).exists():
            return
        else:
            if len(product_name) < 3:
                raise ValidationError(
                    _(
                        '"%(value)s" is not a valid name. When adding a new product please give him a name with at least 3 characters.'
                    ),
                    params={"value": product_name},
                    code="Wrong name for new product",
                )
