from django import forms

from demoapp.models import Product, Employee


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=('name','price')


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'










