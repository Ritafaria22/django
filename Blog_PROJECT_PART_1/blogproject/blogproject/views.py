from django.shortcuts import render
from postapp.models import Post
def home(request):
    data= Post.objects.all()#postapp theke shob post load korlam
    # print(data)
    # for i in data:
    #     print(i.title)
    #     for j in i.category.all():
    #         print(j)
    #     print()
    return render(request, 'home.html', {'data': data})