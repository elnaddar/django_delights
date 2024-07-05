from django.urls import path
from . import views

ingredient_urls = [
    path("ingredients/", views.ingredients.IngredientListView.as_view(), name="ingredients.index"),
    path("ingredients/create", views.ingredients.IngredientCreateView.as_view(), name="ingredients.create"),
    path("ingredients/update/<pk>", views.ingredients.IngredientUpdateView.as_view(), name="ingredients.update"),
    path("ingredients/delete/<pk>", views.ingredients.IngredientDeleteView.as_view(), name="ingredients.delete"),
]


menu_items_urls = [
    path("menu_items/", views.menu_items.MenuItemListView.as_view(), name="menu_items.index"),
    path("menu_items/create", views.menu_items.MenuItemCreateView.as_view(), name="menu_items.create"),
    path("menu_items/update/<pk>", views.menu_items.MenuItemUpdateView.as_view(), name="menu_items.update"),
    path("menu_items/delete/<pk>", views.menu_items.MenuItemDeleteView.as_view(), name="menu_items.delete"),
]

urlpatterns = [
    *ingredient_urls,
    *menu_items_urls
]