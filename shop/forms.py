from email.policy import default

from django import forms

from shop.models import Product, Category
from django import forms
from .models import Product



class ProductForm(forms.Form):
    name = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=14, decimal_places=2)
    image = forms.ImageField(required=False)
    quantity = forms.IntegerField(required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    discount = forms.IntegerField(required=False, min_value=0, max_value=100)
    rating = forms.ChoiceField(choices=Product.Ratingchoice)


    def save(self, commit: object = True) -> Product | None:
        cd = self.cleaned_data
        product = None
        if commit:
            product = Product.objects.create(
                name=cd.get("name"),
                description = cd.get("description"),
                price = cd.get("price"),
                image = cd.get("image"),
                quantity = cd.get("quantity"),
                category = cd.get("category"),
                discount = cd.get("discount"),
                rating = cd.get("rating")
            )
        return product





class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ()




