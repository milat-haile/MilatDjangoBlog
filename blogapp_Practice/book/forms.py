from django import forms
from .models import Tutorial

class BookForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = ['title', 'author', 'published_date', 'description']