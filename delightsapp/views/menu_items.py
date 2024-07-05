from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from extra_views import InlineFormSetFactory, CreateWithInlinesView
from ..models import MenuItem, RecipeRequirement
from ..forms.menu_items import MenuItemForm
from django.urls import reverse_lazy

class MenuItemListView(ListView):
    model = MenuItem
    template_name = "delightsapp/menu_items/index.html"

class RecipeRequirementInline(InlineFormSetFactory):
    model = RecipeRequirement
    fields = ['ingredient', 'quantity']
    factory_kwargs = {'extra': 1, 'can_delete': True}
    prefix = 'recipe_requirements'


class MenuItemCreateView(CreateWithInlinesView):
    model = MenuItem
    form_class = MenuItemForm
    inlines = [RecipeRequirementInline]
    template_name = "delightsapp/menu_items/create.html"
    success_url = reverse_lazy("menu_items.index")

class MenuItemUpdateView(UpdateView):
    model = MenuItem
    template_name = "delightsapp/menu_items/update.html"
    fields = ("title", "weight")
    success_url = reverse_lazy("menu_items.index")

class MenuItemDeleteView(DeleteView):
    model = MenuItem
    template_name = "delightsapp/menu_items/delete.html"
    success_url = reverse_lazy("menu_items.index")
