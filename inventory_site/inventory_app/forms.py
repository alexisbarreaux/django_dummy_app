from django import forms


class EmployeeLoginForm(forms.Form):
    firstname = forms.CharField(label="Firstname", max_length=40)
    lastname = forms.CharField(label="Lastname", max_length=40)
