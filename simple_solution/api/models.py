from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def display_price(self):
        return "{0:.2f}".format(self.price)


class Discount(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class Tax(models.Model):
    name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=5, decimal_places=2)

class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    items = models.ManyToManyField(Item, through='OrderItem')
    discount = models.ForeignKey(Discount, null=True, blank=True, on_delete=models.SET_NULL)
    tax = models.ForeignKey(Tax, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'Order {self.id} | {self.created_at.strftime("%d.%m.%Y %H:%M")}'

    def get_total_cost(self):
        total = sum(item.price for item in self.items.all())

        if self.discount:
            total -= self.discount.amount

        if self.tax:
            total *= (1 + self.tax.rate / 100)

        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    item = models.ForeignKey(Item, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.quantity



