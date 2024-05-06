from django.urls import path
from app.views import *

urlpatterns = [
    path('', index, name='index'),  
    path('add/', profile_add, name='profile_add'),
    path('profile/<int:profile_id>/', profile_view, name='profile_view'),
    path('profile_edit/<int:profile_id>/edit/', profile_edit, name='profile_edit'),
    path('profile_delete/<int:profile_id>/delete/', delete_profile, name='delete_profile'),
    
    path('product/add/', product_add, name='product_add'),  
    path('product/list/', product_list, name='product_list'),  
    path('product/view/<int:product_id>/', product_view, name='product_view'),
    path('product/<int:product_id>/edit',product_edit, name= 'product_edit'),
    path('product_delete/<int:product_id>/delete/', delete_product, name='delete_product'),
    
    path('person/add/', person_add, name='person_add'), 
    path('person/list/', person_list, name='person_list'),
    path('person/view/<int:person_id>/',person_view, name='person_view'),
    path('person/<int:person_id>/edit',person_edit, name= 'person_edit'),
    path('person_delete/<int:person_id>/delete/',delete_person, name='delete_person'), 
    
    

]
