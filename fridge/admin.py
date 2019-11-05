from django.contrib import admin

from . import models


class RequirementInline(admin.StackedInline):
    model = models.Requirement
    extra = 4

    
class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        ("General Info", {'fields': ['name', 'procedure']}),
    ]
    inlines = [RequirementInline]

    
admin.site.register(models.Product)
admin.site.register(models.Ingredient)
admin.site.register(models.Fridge)
admin.site.register(models.Requirement)
admin.site.register(models.Recipe, RecipeAdmin)
