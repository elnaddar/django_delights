from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from ..models import Ingredient
from delightsapp.forms import ingredients
from django.urls import reverse_lazy

class IngredientListView(ListView):
    model = Ingredient
    template_name = "delightsapp/ingredients/index.html"

class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = ingredients.IngredientForm
    template_name = "delightsapp/ingredients/create.html"
    

class IngredientUpdateView(UpdateView):
    model = Ingredient
    template_name = "delightsapp/ingredients/update.html"
    fields = "__all__"


class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = "delightsapp/ingredients/delete.html"
    success_url = reverse_lazy("ingredients.index")
