from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    stock=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    order_date=models.DateTimeField(auto_now_add=True)