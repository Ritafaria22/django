from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d={'author' : 'Rahim', 'age': 4, 'list' : ['python','is','best'], 
       'birthday' : datetime.datetime.now(), 'val': ' ' ,'courses' : [

        {
           'id':1,
           'name' : 'python',
           'fee' : 5000
        },

        {
           'id':2,
           'name' : 'django',
           'fee' : 8000
        },
        
        {
           'id':3,
           'name' : 'c++',
           'fee' : 4000
        }

    ]}
    return render(request, 'home.html', context=d)