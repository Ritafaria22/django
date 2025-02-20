from django.db import models
from category.models import Catagory
#Create your models here.
class Task(models.Model):
    id=models.IntegerField
    title=models.CharField(max_length=40)
    description=models.CharField(max_length=100)
    assigndate = models.DateField() 
    is_completed= models.BooleanField(default=False)
    category=models.ManyToManyField(Catagory)

    def __str__(self):
        return self.title