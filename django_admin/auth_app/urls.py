from django.urls import path
from .views import * 

urlpatterns = [
   
    path('register/', register, name='register'),
    path('customer_list/', customer_list, name='customer_list'),
    path('admin_list/', admin_list, name='admin_list'), 
    path('login',login_u,name='login'),
    path('logout/', logout, name='logout'), 
]  

