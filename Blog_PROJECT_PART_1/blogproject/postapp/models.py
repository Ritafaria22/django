from django.db import models
from categoriesapp.models import Catagory
from authorapp.models import Author

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    category=models.ManyToManyField(Catagory)#1 post can be in many categories and in 1 catagory there can be many post
    author= models.ForeignKey(Author, on_delete=models.CASCADE)#foreighkey diye many to one.mane author er sathe post er relation

    def __str__(self):
        return self.title
