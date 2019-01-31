from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'cname'
        ]

        widgets = {
            'cname': forms.TextInput(attrs={'class': 'form-group', 'placeholder': 'Category Name'}),
        }
