from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,unique=True, null=True, blank=True)
    def __str__(self):
        return self.name
    
    
class Car(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE,  null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    image=models.ImageField(upload_to='uploads/', blank=True, null= True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="cars")
    
    def __str__(self):
        return self.title
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order by {self.user.username} for {self.car.title}"
    

        
class Comment(models.Model):
    post=models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments' )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_on= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username if self.user else "Anonymous"}: {self.text}'

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} bought {self.car.title} on {self.purchase_date}"