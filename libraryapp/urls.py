from django.contrib import admin
from django.urls import path
from . import views

app_name='libraryapp'

urlpatterns = [
    path('list/', views.book_list, name='book_list'),                   
    path('detail/<int:book_id>', views.book_detail, name='book_detail'),                        
    path('register/', views.book_register, name='book_register'),                        
    path('update/<int:book_id>', views.book_update, name='book_update'), 
    path('delete/<int:book_id>', views.book_delete, name='book_delete'),             
    path('result/', views.book_result, name="book_result"),
]