from django import forms
from datetime import date


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
    )
    expiry_date: date = forms.DateField(
        initial=date.today(), label="Product expiry date"
    )


class ProductAddingForm(forms.Form):
    """Form for employees when a product was added in stock."""

    GTIN: str = forms.CharField(
        label="GTIN",
        max_length=14,
        widget=forms.TextInput(attrs={"placeholder": "Remember, 14 digits at most"}),
    )
    name: str = forms.CharField(label="Product name", max_length=100)
