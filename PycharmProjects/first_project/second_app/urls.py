from django.urls import path
from second_app.views import index,user



urlpatterns = [
    path('index/',index,name='index'),
    path('users/',user,name='user')
]