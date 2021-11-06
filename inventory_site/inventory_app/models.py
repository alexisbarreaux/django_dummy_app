from django.db import models
from datetime import date
from django.contrib import admin
from typing import Optional


class Product(models.Model):
    """Model storing data about one product type.

    Attributes:
        current_store (str) : shop in which the product is displayed.
        product_name (str): name of the product in the shop it is in.
        GTIN (str): unique identifier of the product.
        shortest_expiry_date (Optional[date]): Date when the first displayed product
            of this type (this GTIN) will expire in the shope. Defaults to current date.

    """

    def current_date():
        return date.today()

    current_store: str = models.CharField("Shop", max_length=200)
    product_name: str = models.CharField("Name", max_length=200)
    GTIN: str = models.CharField(max_length=14)
    shortest_expiry_date: Optional[date] = models.DateField(
        "Products expire at", default=current_date
    )
    #    expiry_dates: List[date]
    # )
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.product_name

    @admin.display(
        boolean=True,
        ordering="shortest_expiry_date",  # Order by date on click
        description="Expires today",  # To change name
    )
    def expires_today(self):
        now = date.today()
        return now == self.shortest_expiry_date
