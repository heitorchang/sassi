from django.contrib import admin
from .models import Market, ProductCategory, Product, Brand, Price

admin.site.register((Market, ProductCategory, Product, Brand, Price))
