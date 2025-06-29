from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description =models.TextField()
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/')


    def __str__(self):
        return self.name 
    
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this line
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
    