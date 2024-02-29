from django.db import models
from Users.models import CustomUser
from Products.models import Product

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='CartItem')
    created_at = models.DateTimeField(null=True, blank=True)

    def calculate_total_price(self):
        total_price = 0
        for cart_item in self.cart_items.all():
            total_price += cart_item.product.price * cart_item.quantity
        return total_price

    def __str__(self):
        return f"Cart for {self.user.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.title} in Cart"