from django.shortcuts import render
from carapp.models import Car,Brand


def home(request, brand_slug=None):#brand_slug none mane catagory select na korle initially shb post dekhabe
    data= Car.objects.all()#carapp theke shob post load korlam
    if brand_slug is not None:
        brand = Brand.objects.get(slug = brand_slug)
        data= Car.objects.filter(brand = brand)
    
    brands=Brand.objects.all()
    return render(request, 'home.html', {'data': data, 'brand': brands})

