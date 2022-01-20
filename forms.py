from django import forms
from .models import Inventory


class ProductForm(forms.ModelForm):

        class Meta:
            model = Inventory
            fields = { 'location','quantity','product_code','productname'}
            labels = {
                'productname':'Product Name',
                'product_code':'Product Code',
                'quantity' : 'Quantity',
                'location' : 'Warehouse / Location'
            }

            def __init__(self, *args, **kwargs):
                super(ProductForm,self).__init__(*args, **kwargs)
                self.fields['location'].empty_label = "Select"
                self.fields['product_code'].required = False
           