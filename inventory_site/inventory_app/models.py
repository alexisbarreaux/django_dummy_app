from django.db import models
from datetime import date, datetime
from django.contrib import admin
from typing import Optional


class Store(models.Model):
    """Class storing data about a store.

    Attributes:
        name (str): Name of the store.
    """

    # Mostly empty
    name: str = models.CharField("Store name", max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    """Class to store data about an employee

    Attributes:
        firstname (str): First name of the employee.
        lastname (str): Last name of the employee.
        current_store (str): Name of the store in which the employee works.
    """

    current_store: str = models.ForeignKey(Store, on_delete=models.CASCADE)
    firstname: str = models.CharField("First name", max_length=40)
    lastname: str = models.CharField("Last name", max_length=40, unique=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Product(models.Model):
    """Model storing data about one product type.

    Attributes:
        current_store (str) : shop in which the product is displayed.
        name (str): name of the product in the shop it is in.
        GTIN (str): unique identifier of the product.
        shortest_expiry_date (Optional[date]): Date when the first displayed product
            of this type (this GTIN) will expire in the shope. Defaults to current date.
        last_modified  (datetime): Datetime to know when this object was last modified.
    """

    def current_date():
        return date.today()

    current_store: str = models.ForeignKey(Store, on_delete=models.CASCADE)
    name: str = models.CharField("Name", max_length=100)
    GTIN: str = models.CharField(max_length=14)
    shortest_expiry_date: Optional[date] = models.DateField(
        "Products expire at", default=current_date
    )
    last_modified: datetime = models.DateTimeField(auto_now=True)
    #    expiry_dates: List[date]
    # )

    def __str__(self):
        return self.name

    @admin.display(
        boolean=True,
        ordering="shortest_expiry_date",  # Order by date on click
        description="Expires today",  # To change name
    )
    def expires_today(self):
        now = date.today()
        return now == self.shortest_expiry_date
