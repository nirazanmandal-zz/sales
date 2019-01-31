from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'category',
            'pname',
            'quantity',
            'price',
            'total',
            'description',
        ]

        widgets = {
            'category': forms.Select(attrs={'class': 'form-group', 'placeholder': 'Select Category'}),
            'pname': forms.TextInput(attrs={'class': 'form-group', 'placeholder': 'Product Name'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-group'}),
            'total': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['category'].empty_label = 'Select Category'
        self.fields['pname'].empty_label = 'Product Name'
