from datetime import date, timedelta
from django.shortcuts import render

from .models import Fridge, Recipe, DiaryEntry


def index(request):
    diary_start = date.today() - timedelta(days=31)
    fridges = Fridge.objects.all()
    recipes = Recipe.objects.all()
    entries = DiaryEntry.objects.filter(cooked_on__gte=diary_start)
    return render(request, 'fridge/index.html',
                  {'fridges': fridges,
                   'recipes': recipes,
                   'entries': entries})


def printable(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'fridge/printable.html',
                  {'recipe': recipe})
