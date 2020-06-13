from django import forms
from .models import Post,Chat

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class ChatForm(forms.ModelForm):

    class Meta:
        model = Chat
        fields = ('title', 'text',)
