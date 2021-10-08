from django.contrib import admin
from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('list/', views.notice_list, name='notice_list'),                   
    path('detail/<int:notice_id>', views.notice_detail, name='notice_detail'),                        
    path('register/', views.notice_register, name='notice_register'),                        
    path('update/<int:notice_id>', views.notice_update, name='notice_update'), 
    path('delete/<int:notice_id>', views.notice_delete, name='notice_delete'),
    path('weather/', views.weather, name='weather'),
    path('transport/', views.transport, name='transport'),             
 
]