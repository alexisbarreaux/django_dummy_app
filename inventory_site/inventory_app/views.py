from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.views import LoginView

from .models import Employee, Store, Product

# Create your views here.
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
