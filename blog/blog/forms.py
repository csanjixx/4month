from django import forms
from blog.models import Product,Category,Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'text', 'image' ,'rate','cat']
        widgets = {
            'title': forms.TextInput,
            'text': forms.Textarea
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['text','post']
        widgets = {
            'text': forms.TextInput
        }
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        widgets = {
            'text': forms.Textarea
        }