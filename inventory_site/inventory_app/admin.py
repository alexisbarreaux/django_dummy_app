from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Constant data", {"fields": ["GTIN"]}),
        (
            "Store dependent date",
            {"fields": ["current_store", "product_name", "shortest_expiry_date"]},
        ),
    ]
    # To change display in the main page of the products objects instead
    # of just the __str__ result
    list_display = ("GTIN", "current_store", "expires_today")
    # Adds a filter tab
    list_filter = ["shortest_expiry_date"]
    # clear
    search_fields = ["current_store", "GTIN"]


admin.site.register(Product, ProductAdmin)
