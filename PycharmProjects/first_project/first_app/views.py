from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    a=5+5
    my_dict={'insert_me':'inserted from view','second_key':'again from view'}
    return render(request,'first_app/index.html',my_dict)

def home(request):
    return HttpResponse("welcome to home page")

def img(request):
    return render(request,'first_app/static_image.html')

