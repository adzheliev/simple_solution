"""Registering instances in admin panel"""

from django.contrib import admin
from .models import (
    Item,
    Order,
    OrderItem,
    Tax,
    Discount,
    OrderTax,
    OrderDiscount
)


class OrderItemInline(admin.TabularInline):
    """Inline class for Order"""
    model = OrderItem


class DiscountInline(admin.TabularInline):
    """Inline class for Order"""
    model = OrderDiscount


class TaxInline(admin.TabularInline):
    """Inline class for Order"""
    model = OrderTax


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Registering Order Model in admin panel"""
    inlines = [OrderItemInline, DiscountInline, TaxInline]


admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Discount)
admin.site.register(Tax)
