
from dataclasses import field
from django import forms
from .models import Blog, Comment

class BlogForm(forms.ModelForm):
    tags = forms.CharField(max_length=255)
    tags = forms.CharField(label='tags ni kiriting',
                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tags ni kiriting'}))
    class Meta:
        model = Blog
        fields = ['title','description', 'image', 'category','tags', 'is_published']
        
        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter the title'}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'write a description'}),
        'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'enter the images'}),
        'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' enter the category'}),
        'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholderenter': 'enter the tags'})
        }
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'rating']
        
    
class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'image', 'category']
    