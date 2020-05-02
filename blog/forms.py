from django import forms
from .models import Post, Comment
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class SignUpForm(UserCreationForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'category', 'title', 'text', 'image')
        # labels = {'author': '投稿者', 'category': 'カテゴリ', 'title': 'タイトル', 'text': '本文', 'image': 'ヘッダー画像'}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)
        # labels = {'author': '投稿名', 'text': '本文'}