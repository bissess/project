from django import forms
from .models import Post, PostCategory, Comment


class CreationPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'description', 'image', 'category']

        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Image',
            'category': 'Category',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'post__title'}),
            'description': forms.Textarea(attrs={'class': 'post__description'}),
            'image': forms.ClearableFileInput(attrs={'class': 'post__image'}),
            'category': forms.Select(attrs={'class': 'post__category'})
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']

        labels = {
            'text': 'Comment',
        }

        widgets = {
            'text': forms.Textarea(attrs={'class': 'comment-input', 'placeholder': 'Your Comment ...'})
        }