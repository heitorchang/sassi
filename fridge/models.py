from django.db import models


class Product(models.Model):
    """Abstract representation of (typically raw) food items
    Keep names in lowercase singular.
    cabbage, onion, rice
    """

    name = models.CharField(max_length=78)

    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name


class Fridge(models.Model):
    """State of refrigerator and other storage"""

    name = models.CharField(max_length=31)

    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return "{} ({} items)".format(self.name, self.ingredient_set.count())


class Ingredient(models.Model):
    """Specific amount, weight, etc. of a Product"""

    fridge = models.ForeignKey(Fridge, on_delete=models.CASCADE)
    amount = models.CharField(max_length=78)  # units, weight or volume
    product = models.ForeignKey(Product, on_delete=models.CASCADE)



    class Meta:
        ordering = ['fridge', 'product', '-amount']
        
    def __str__(self):
        return f"{self.amount} {self.product} ({self.fridge.name})"


class Recipe(models.Model):
    """Description of a recipe"""

    name = models.CharField(max_length=78)
    procedure = models.TextField(blank=True)


    def missing(self):
        requirements = self.requirement_set.all()
        available_ingredients = Ingredient.objects.all()
        required_products = set(req.product.name for req in requirements)
        available_products = set(ingr.product.name for ingr in available_ingredients)
        return sorted(required_products - available_products)
    
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return f"{self.name}"


class Requirement(models.Model):
    """Specific ingredient for a Recipe"""
    
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    amount = models.CharField(max_length=78)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


    class Meta:
        ordering = ['recipe', 'product', 'amount']

    def __str__(self):
        return f"{self.amount} {self.product} ({self.recipe.name})"
