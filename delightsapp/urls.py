from django.urls import path
from . import views

ingredient_urls = [
    path("ingredients/", views.ingredients.IngredientListView.as_view(), name="ingredients.index"),
    path("ingredients/create", views.ingredients.IngredientCreateView.as_view(), name="ingredients.create"),
    path("ingredients/update/<pk>", views.ingredients.IngredientUpdateView.as_view(), name="ingredients.update"),
    path("ingredients/delete/<pk>", views.ingredients.IngredientDeleteView.as_view(), name="ingredients.delete"),
]

urlpatterns = [
    *ingredient_urls
]