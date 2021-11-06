from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.views import LoginView

from .models import Employee, Store, Product
from .forms import EmployeeLoginForm

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
            if (
                employee := Employee.objects.filter(
                    firstname=form.cleaned_data["firstname"],
                    lastname=form.cleaned_data["lastname"],
                ).first()
                is not None
            ):
                return HttpResponseRedirect("index")
            else:
                # If the user doesn't exist display an error message to the user
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


class EmployeeLogin(LoginView):
    template_name = "inventory_app/login.html"


class IndexView(generic.ListView):
    template_name = "inventory_app/index.html"
    context_object_name = "products_from_store"
    store = 1

    def get_queryset(self):
        """Return the last five published questions."""
        return Product.objects.filter(current_store=self.store).order_by(
            "shortest_expiry_date"
        )[:20]
