from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    posts = [
        {
            'title':'Post 1',
            'author':'Finley Wood',
            'content':'This is the first post',
            'date':'20 September 2020',
        },
        {
            'title':'Post 2',
            'author':'John Doe',
            'content':'This is the second post',
            'date':'27 September 2020',
        },
    ]
    context = {
        'title':'Home',
        'posts':posts,
    }
    return render(request, 'main/home.html', context)

def about(request):
    context = {
        'title':'About',
    }
    return render(request, 'main/about.html', context)

def contactus(request):
    return HttpResponse('<h1>This is the contact us page!</h1>')
