from django.urls import path
from . import views

app_name = 'tesdir'

urlpatterns = [
    path('', views.index, name='index'),
    path('transacoes/', views.transacoes, name='transacoes'),
]
