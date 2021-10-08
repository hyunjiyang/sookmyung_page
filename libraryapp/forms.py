from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'publisher', 'pub_year', 
                'location', 'describe', 'photo']