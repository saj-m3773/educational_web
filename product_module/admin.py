from django.contrib import admin
from django.http import HttpRequest

from . import models
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active', 'author']
    prepopulated_fields = {"slug": ["title"]}

    def save_model(self, request: HttpRequest, obj: Product, form, change):
        obj.author = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory)
admin.site.register(models.File)
admin.site.register(models.ProductComment)
