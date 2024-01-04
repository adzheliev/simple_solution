from django.contrib import admin
from .models import Item, Order, OrderItem, Tax, Discount


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class DiscountInline(admin.TabularInline):
    model = Discount


class TaxInline(admin.TabularInline):
    model = Tax


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline, DiscountInline, TaxInline]


admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Discount)
admin.site.register(Tax)
