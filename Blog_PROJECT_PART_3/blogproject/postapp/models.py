from django.db import models
from categoriesapp.models import Catagory
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    category=models.ManyToManyField(Catagory)#1 post can be in many categories and in 1 catagory there can be many post
    author= models.ForeignKey(User, on_delete=models.CASCADE)#foreighkey diye many to one.mane author er sathe post er relation
    image=models.ImageField(upload_to='postapp/media/uploads/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments' )
    name=models.CharField(max_length=30)
    email=models.EmailField()
    body=models.TextField()
    created_on= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comments by {self.name}"

