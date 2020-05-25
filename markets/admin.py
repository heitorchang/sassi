from django.contrib import admin
from .models import Market, ProductCategory, Product, Brand, Price

class MarketAdmin(admin.ModelAdmin):
    fields = ['name', 'address']


class PriceAdmin(admin.ModelAdmin):
    search_fields = ['product__name', 'market__name']
    

admin.site.register(Market, MarketAdmin)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Price, PriceAdmin)
