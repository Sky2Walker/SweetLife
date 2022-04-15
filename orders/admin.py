from django.contrib import admin

# Register your models here.
from orders.models import ProductInOrder


class ProductInOrderS (admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]

    class Meta:
        model = ProductInOrder

admin.site.register(ProductInOrder, ProductInOrderS)