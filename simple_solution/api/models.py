from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def display_price(self):
        return "{0:.2f}".format(self.price)


class Order(models.Model):
    items = models.ManyToManyField('Item')
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_total_cost(self):
        total_cost = 0
        for item in self.items.all():
            total_cost += item.price
        return total_cost
