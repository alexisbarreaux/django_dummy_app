from django.urls import path
from . import views

app_name = "inventory"
urlpatterns = [
    path("", views.get_index, name="index"),
    path("login", views.get_employee, name="login"),
    path(
        "store_display/<str:store_name>", views.get_store_display, name="store_display"
    ),
    path(
        "store_display/<str:store_name>/add_date",
        views.add_expiry_date_for_product,
        name="add_date",
    ),
]
