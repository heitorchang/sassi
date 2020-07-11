from datetime import date, timedelta
from django.shortcuts import render
from django.db.models import Count

from .models import Fridge, Recipe, DiaryEntry


def index(request):
    diary_start = date.today() - timedelta(days=90)
    fridges = Fridge.objects.all()
    recipes = Recipe.objects.all()
    sortedrecipes = Recipe.objects.annotate(count=Count('diaryentry__id')).order_by('-count', 'name')
    entries = DiaryEntry.objects.filter(cooked_on__gte=diary_start)
    return render(request, 'fridge/index.html',
                  {'fridges': fridges,
                   'recipes': recipes,
                   'sortedrecipes': sortedrecipes,
                   'entries': entries})


def printable(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'fridge/printable.html',
                  {'recipe': recipe})


def sortedbytimes(request):
    return render(request, 'fridge/sortedbytimes.html')
