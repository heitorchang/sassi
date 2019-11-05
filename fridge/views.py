from django.shortcuts import render

from .models import Fridge, Recipe


def index(request):
    fridges = Fridge.objects.all()
    recipes = Recipe.objects.all()
    return render(request, 'fridge/index.html',
                  {'fridges': fridges,
                   'recipes': recipes})
