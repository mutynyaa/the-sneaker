from django.contrib import admin
from .models import *

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display=[field.name for field in ProductCategory._meta.fields]


    class Meta:
        model=ProductCategory

admin.site.register(ProductCategory, ProductCategoryAdmin)

class ProductImageInline(admin.TabularInline):
    model=ProductImage
    extra=0


class ProductAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Product._meta.fields]
    inlines=[ProductImageInline]

    class Meta:
        model=Product

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)

