from django import forms 
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']
        #fields = '__all__'
        #fields = ['name','bio']