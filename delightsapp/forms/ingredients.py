from django import forms
from ..models import Ingredient


class IngredientForm(forms.ModelForm):
    """Form definition for Ingredient."""

    class Meta:
        """Meta definition for Ingredientform."""
        model = Ingredient
        fields = "__all__"
