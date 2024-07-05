from django import forms
from django.forms import inlineformset_factory
from ..models import MenuItem, RecipeRequirement

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['title', 'description', 'weight']

RecipeRequirementFormSet = inlineformset_factory(
    MenuItem,
    RecipeRequirement,
    fields=['ingredient', 'quantity'],
    extra=1,
    can_delete=True
)
