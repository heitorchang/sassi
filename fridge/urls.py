from django.urls import path
from . import views

app_name = 'fridge'

urlpatterns = [
    path('', views.index, name='index'),
    path('printable/<int:recipe_id>/', views.printable, name="printable"),
]
