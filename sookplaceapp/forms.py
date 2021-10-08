from django import forms
from .models import Sookplace

class SookplaceForm(forms.ModelForm):
    class Meta:
        model = Sookplace
        fields = ['title', 'address', 'detail_addr', 'describe', 'photo']
    
