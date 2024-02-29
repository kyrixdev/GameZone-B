from django import forms
from .models import Manufacturer, Category, Genre, ProductColor, ProductSize, SubCategory

class ProductFilterForm(forms.Form):
    manufacturer = forms.ModelMultipleChoiceField(
        queryset=Manufacturer.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label='Manufacturers',
    )
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label='Categories',
    )
    subcategory = forms.ModelMultipleChoiceField(
        queryset=SubCategory.objects.all(),  # Include all subcategories
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label='Subcategories',
    )
    genre = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label='Genres',
    )
    colors = forms.ModelMultipleChoiceField(
        queryset=ProductColor.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label='Colors',
    )
    sizes = forms.ModelMultipleChoiceField(
        queryset=ProductSize.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label='Sizes',
    )
    min_price = forms.DecimalField(
        required=False,
        min_value=0,
        max_value=99999,
        decimal_places=2,
        label='Minimum Price'
    )
    max_price = forms.DecimalField(
        required=False,
        min_value=0,
        max_value=99999,
        decimal_places=2,
        label='Maximum Price'
    )