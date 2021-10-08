from django.contrib import admin
from django.urls import path
from . import views

app_name = 'sookplaceapp'

urlpatterns = [
    path('list/', views.sookplace_list, name='sookplace_list'),                   
    path('detail/<int:sookplace_id>', views.sookplace_detail, name='sookplace_detail'),                        
    path('register/', views.sookplace_register, name='sookplace_register'),                        
    path('update/<int:sookplace_id>', views.sookplace_update, name='sookplace_update'), 
    path('delete/<int:sookplace_id>', views.sookplace_delete, name='sookplace_delete'),             
]