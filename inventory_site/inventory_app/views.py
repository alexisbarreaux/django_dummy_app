from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Employee, Product, Store
from .forms import EmployeeLoginForm, ExpiryDateAddingForm


def get_index(request: HttpRequest):
    """Redirects to login."""
    # TODO add a way to remember that user is logged in.
    return HttpResponseRedirect(reverse("inventory:login"))


# Create your views here.
def get_employee(request: HttpRequest):
    """Method to display a form to get the name of an employee and find
    in which store he/she works.

    Either redirects to the login if the name doesn't match an employee in
    the database or sends to the main display of the store.
    """
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = EmployeeLoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            try:
                # TODO assert this returns at most one object
                employee = Employee.objects.get(
                    firstname=form.cleaned_data["firstname"],
                    lastname=form.cleaned_data["lastname"],
                )
                return HttpResponseRedirect(
                    reverse("inventory:store_display", args=(employee.current_store,))
                )
            except Employee.DoesNotExist:
                # If the employee doesn't exist display an error message to the user
                return render(
                    request,
                    "inventory_app/login.html",
                    {
                        "form": form,
                        "error_message": "Employee does not exist. Please enter a valid first and last name.",
                    },
                )

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmployeeLoginForm()

    return render(request, "inventory_app/login.html", {"form": form})


def get_store_display(request: HttpRequest, store_name: str):
    """Function to display the data about a store for an employee."""

    def get_first_products(store: Store):
        """Return the 20 products with the shortest expiry dates
        of the store.

        Args:
            store (Store): store in which to search for the products."""
        return Product.objects.filter(current_store=current_store.id).order_by(
            "shortest_expiry_date"
        )[:20]

    current_store = Store.objects.filter(name=store_name).first()
    if current_store is None:
        context = {}
    else:
        context = {
            "store_name": current_store.name,
            "products_list": get_first_products(current_store),
        }

    return render(request, "inventory_app/store_display.html", context)


def add_expiry_date_for_product(request: HttpRequest, store_name: str):
    """Function to add a an expiry date for a product."""
    # TODO remove this and directly match id
    current_store = Store.objects.filter(name=store_name).first()
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ExpiryDateAddingForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            try:
                product = Product.objects.get(
                    GTIN=form.cleaned_data["GTIN"],
                )
                product.update_expiry_date(form.cleaned_data["expiry_date"])
            except Product.DoesNotExist:
                product = Product.objects.create(
                    current_store=current_store,
                    GTIN=form.cleaned_data["GTIN"],
                    shortest_expiry_date=form.cleaned_data["expiry_date"],
                    name=form.cleaned_data["product_name"],
                )
            finally:
                # TODO add message for successful adding
                return HttpResponseRedirect(
                    reverse("inventory:store_display", args=(store_name,))
                )

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ExpiryDateAddingForm()

    return render(request, "inventory_app/expiry_date_adding.html", {"form": form})
