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
    # update method
    def update(self, product):
        data = self.cleaned_data
        product.name = data['name']
        product.description = data['description']
        product.price = data['price']
        product.save()
        return product
    
    # delete method
    def delete(self, product):
        product.delete()
        return product
    
    # get method
    def get(self, pk):
        return Product.objects.get(pk=pk)