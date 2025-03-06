from django.db import models
from decimal import Decimal



# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)


    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title


    class Meta:
        db_table = 'category'
        ordering = ['-id']



class Product(BaseModel):


    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='images/', null=True, blank=True, default='images/default png.png')
    discount = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True)

    @property
    def discounted_price(self):
        if self.discount > 0:
            self.price = self.price * Decimal(1 - self.discount / 100)
        return Decimal(f'{self.price}').quantize(Decimal('0.00'))


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'
        ordering = ['-id']  # ID bo‘yicha kamayish tartibida saralaydi
        verbose_name = "Product"
        verbose_name_plural = "Products"




class Comment(BaseModel):
    class Ratingchoice(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
    full_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField()
    content = models.TextField()
    rating = models.PositiveIntegerField(choices=Ratingchoice.choices, default=Ratingchoice.ONE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='comments')
    is_private = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.email} => {self.rating} => {self.product.name}'