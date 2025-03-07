from django.shortcuts import render
from postapp.models import Post
from categoriesapp.models import Catagory
 
def home(request, category_slug=None):#category_slug none mane catagory select na korle initially shb post dekhabe
    data= Post.objects.all()#postapp theke shob post load korlam
    if category_slug is not None:
        category = Catagory.objects.get(slug = category_slug)
        data= Post.objects.filter(category = category)
    
    categories=Catagory.objects.all()
    return render(request, 'home.html', {'data': data, 'category': categories})



 