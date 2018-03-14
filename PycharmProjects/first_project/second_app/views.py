from django.shortcuts import render
from second_app.models import User



# Create your views here.

def index(request):
    return render(request,'second_app/index.html')

def user(request):
    userlist = User.objects.order_by('first_name')
    mydict = {'user_list':userlist}
    return render(request,'second_app/show_users.html',context=mydict)