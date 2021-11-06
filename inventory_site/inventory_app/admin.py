from django.contrib import admin
from .models import Product, Employee, Store


class StoreAdmin(admin.ModelAdmin):
    search_fields = ["name"]


class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ["lastname"]


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Constant data", {"fields": ["GTIN"]}),
        (
            "Store dependent date",
            {"fields": ["current_store", "name", "shortest_expiry_date"]},
        ),
    ]
    # To change display in the main page of the products objects instead
    # of just the __str__ result
    list_display = ("GTIN", "current_store", "shortest_expiry_date", "expires_today")
    # Adds a filter tab
    list_filter = ["shortest_expiry_date"]
    # clear
    search_fields = ["current_store", "GTIN"]


admin.site.register(Store, StoreAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Product, ProductAdmin)
