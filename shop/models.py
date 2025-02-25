from django.db import models
from decimal import Decimal



# Create your models here.

class Product(models.Model):
    class Ratingchoice(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    discount = models.PositiveIntegerField(default=0)
    rating = models.PositiveIntegerField(choices=Ratingchoice.choices, default=Ratingchoice.ONE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def discounted_price(self):
        if self.discount > 0:
            self.price = self.price * Decimal(1 - self.discount / 100)
        return Decimal(f'{self.price}').quantize(Decimal('0.00'))


    def __str__(self):
        return self.name

