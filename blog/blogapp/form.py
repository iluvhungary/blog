from django import forms
from .models import Product

class ProductForm(forms.ModelForm): # creating a db with name ProductForm
    # class Meta, It allows you to define various options and configurations that control the behavior of the form or how it interacts with the associated model.
    # Meta can also include additional configuration options such as exclude, widgets, labels, help_texts, error_messages, etc.,
    class Meta:
        model = Product  # it tells the form is associated with model Product
        fields = ['name', 'desc', 'img']  # Lists the fields from the Product model that should be included in the form
