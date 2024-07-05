from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=250, unique=True)
    quantity = models.FloatField(default=0)
    price = models.FloatField()
    unit = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    title = models.CharField(max_length=250, unique=True)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.title

    def update_price(self):
        recipe_requirements = RecipeRequirement.objects.filter(menu_item=self)
        total_price = sum(req.ingredient.price * req.quantity for req in recipe_requirements)
        self.price = total_price * 1.2
        self.save()

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} for {self.menu_item.title}"

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.menu_item.title} purchased on {self.timestamp}"
    
@receiver(post_save, sender=Ingredient)
@receiver(post_save, sender=RecipeRequirement)
@receiver(post_delete, sender=Ingredient)
@receiver(post_delete, sender=RecipeRequirement)
def update_menu_item_price(sender, instance, **kwargs):
    if isinstance(instance, RecipeRequirement):
        menu_item = instance.menu_item
    elif isinstance(instance, Ingredient):
        recipe_requirements = RecipeRequirement.objects.filter(ingredient=instance)
        for requirement in recipe_requirements:
            menu_item = requirement.menu_item
            menu_item.update_price()
        return

    menu_item.update_price()
