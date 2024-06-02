from django import forms

from myapp.models import Product

class ProductForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField()

    # save method
    def save(self):
        data = self.cleaned_data
        product = Product(name=data['name'], description=data['description'], price=data['price'])
        product.save()
        return product