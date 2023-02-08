from django.contrib import admin
from main.models import Post, Person, Car, Product, Order, OrderPosition


# admin.site.register(Post)
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'model', 'color']
    list_filter = ['brand', 'model']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'car']
    list_filter = ['car']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ...


class OrderPositionInline(admin.TabularInline):
    model = OrderPosition
    extra = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price']
    list_filter = ['category']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id']
    inlines = [OrderPositionInline,]


