from django.contrib import admin
from .models import Product, Employee, Store


class EmployeeInline(admin.TabularInline):
    model = Employee
    extra = 1


class StoreAdmin(admin.ModelAdmin):
    """Admin display for stores."""

    search_fields = ["name"]

    # Displaying employees in store
    inlines = [EmployeeInline]
    # Displaying products would make it hard to read for real datasets.


class EmployeeAdmin(admin.ModelAdmin):
    """Admin display for employees."""

    search_fields = ["lastname"]
    # To change display in the main page of the products objects instead
    # of just the __str__ result
    list_display = ("firstname", "lastname", "current_store")
    # Adds a filter tab
    list_filter = ["current_store"]


class ProductAdmin(admin.ModelAdmin):
    """Admin display for products."""

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
