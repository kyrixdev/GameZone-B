from django.contrib import admin
from .models import Manufacturer, Category, ProductColor, SubImage, Product, Review, ProductSize, Genre, SubCategory
# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(Category)
admin.site.register(ProductColor)
admin.site.register(SubImage)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(ProductSize)
admin.site.register(Genre)
admin.site.register(SubCategory)