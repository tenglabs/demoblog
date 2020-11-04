from django import forms
from .models import Comment

from django.forms import Textarea

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'text')
        widgets = {
            'text': Textarea(attrs={ 'rows': 13,'placeholder': 'Type your comment here...'}),
        }
