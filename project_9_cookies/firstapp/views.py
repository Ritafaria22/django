from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse
# Create your views here.
def home(request):
    response=  render(request,'home.html')
    response.set_cookie('name','rahim')
    # response.set_cookie('name','karim', max_age=10)cookies 10 second rakhte chaile
    response.set_cookie('name','karim', expires=datetime.utcnow()+timedelta(days=7))
    return response
     
def get_cookie(request):
    name=request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, 'getcookie.html', {'name': name})

def delete_cookie(request):
    response=render(request, 'del.html')
    response.delete_cookie('name')
    return response

def set_session(request)               :
    # data= {
    #     'name': 'rahim',
    #     'age': 23,
    #     'language' : 'Bangla'
    # }
    # request.session.update(data)
    request.session['name']= 'karim'
    return render(request,'home.html')

def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name', 'Guest')
        request.session.modified=True# mane 10 e=sec er modde arekbar refresh dile next 10 sec active thakbe session time
        return render(request, 'get_session.html', {'name': name })
    else:
        return HttpResponse("Your session has expired ")



def delete_session(request):
    # del request.session['name'] sudhu name delete korte
    
    request.session.flush() # pura session delete korte
     
    return render(request, 'del.html')