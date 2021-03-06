from datetime import date, datetime, timezone
from typing import Optional

from django.contrib import admin
from django.db import models
from django.core.validators import MinLengthValidator

from .validators import validate_GTIN, validate_date_not_passed


class Store(models.Model):
    """Class representing a store..

    Attributes:
        name (str): Name of the store.
    """

    # TODO add localisation ?
    name: str = models.CharField("Store name", max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    """Class to store data about an employee

    Attributes:
        firstname (str): First name of the employee.
        lastname (str): Last name of the employee.
        current_store (Store): Store in which the employee works.
    """

    # TODO add personnal and store related informations ?
    current_store: Store = models.ForeignKey(Store, on_delete=models.CASCADE)
    firstname: str = models.CharField("First name", max_length=40)
    lastname: str = models.CharField("Last name", max_length=40, unique=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Product(models.Model):
    """Model storing data about one product type.

    Attributes:
        current_store (Store) : Store in which the product is displayed.
        name (str): name of the product in the shop it is in.
        GTIN (str): unique identifier of the product.
        shortest_expiry_date (Optional[date]): Date when the first displayed product
            of this type (this GTIN) will expire in the shope. Defaults to current date.
        last_modified  (datetime): Datetime to know when this object was last modified.
    """

    def current_date():
        return date.today()

    current_store: Store = models.ForeignKey(Store, on_delete=models.CASCADE)
    # A product name should have at least three characters
    name: str = models.CharField(
        "Name", max_length=100, validators=[MinLengthValidator(limit_value=3)]
    )
    GTIN: str = models.CharField(
        max_length=14,
        validators=[validate_GTIN],
    )
    shortest_expiry_date: Optional[date] = models.DateField(
        "Products expire at",
        default=current_date,
        validators=[validate_date_not_passed],
    )
    last_modified: datetime = models.DateTimeField(auto_now_add=True)
    # TODO store and delete date in a queue
    #    expiry_dates: set[date]
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

    def update_expiry_date(self, expiry_date: date):
        """Method to update product if needed when receiving a new
        expiry date.

        Args:
            expiry_date (date): Date object to check against current expiry date.
        """
        # Update date if eithers it was valid but a valid and shorter one came
        # up or if it was passed and new valid one is gave.
        if (self.shortest_expiry_date < date.today() <= expiry_date) or (
            date.today() <= expiry_date < self.shortest_expiry_date
        ):
            self.shortest_expiry_date = expiry_date
            self.last_modified = datetime.now(timezone.utc)
            self.save()
        return

    class Meta:
        # Can only have one object for each product/GTIN in a store.
        unique_together = (
            "GTIN",
            "current_store",
        )
