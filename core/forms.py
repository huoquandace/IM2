from django import forms
from django.utils.translation import gettext_lazy as _
from core.models import *

class CategoryAddForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder': _('Category title')})
        self.fields['label'].widget.attrs.update({'placeholder': _('Category label')})
        self.fields['description'].widget.attrs.update({'rows': '3'})
        self.fields['image'].widget.attrs.update({'onchange': 'readURL(this);'})
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_product'].widget.attrs.update({'placeholder': _('Product ID')})
        self.fields['name'].widget.attrs.update({'placeholder': _('Product name')})
        self.fields['brand'].widget.attrs.update({'placeholder': _('Product brand')})
        self.fields['price'].widget.attrs.update({'placeholder': _('Product price'), 'type': 'number',})
        self.fields['description'].widget.attrs.update({'rows': '4'})
        self.fields['image'].widget.attrs.update({'onchange': 'readURL(this);'})
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class SupplierAddForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_supplier'].widget.attrs.update({'placeholder': _('Supplier ID')})
        self.fields['name'].widget.attrs.update({'placeholder': _('Supplier name')})
        self.fields['phone'].widget.attrs.update({'placeholder': _('Supplier phone')})
        self.fields['email'].widget.attrs.update({'placeholder': _('Supplier email'), 'type': 'email'})
        self.fields['fax'].widget.attrs.update({'placeholder': _('Supplier fax')})
        self.fields['address'].widget.attrs.update({'placeholder': _('Supplier address'), 'rows': '4'})
        self.fields['logo'].widget.attrs.update({'onchange': 'readURL(this);'},)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class QuoteAddForm(forms.ModelForm):
    class Meta:
        model = POrder
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

