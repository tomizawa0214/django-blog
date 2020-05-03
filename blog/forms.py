from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        # self.fields['title'].widget.attrs = {'placeholder': '必ずご入力ください。'}
        self.fields['author'].required = False
        self.fields['category'].required = False
        self.fields['title'].required = False
        self.fields['text'].required = False

    def clean_author(self):
        author = self.cleaned_data['author']
        if author == None:
            raise forms.ValidationError ('※投稿者をを選択してください。')
        return author

    def clean_category(self):
        category = self.cleaned_data['category']
        if category == None:
            raise forms.ValidationError ('※カテゴリを選択してください。')
        return category

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) == 0:
            raise forms.ValidationError ('※タイトルを入力してください。')
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) == 0:
            raise forms.ValidationError ('※本文を入力してください。')
        return text

    class Meta:
        model = Post
        fields = ('author', 'category', 'title', 'text', 'image')

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['author'].required = False
        self.fields['text'].required = False

    def clean_author(self):
        author = self.cleaned_data['author']
        if len(author) == 0:
            raise forms.ValidationError ('※名前を入力してください。')
        return author

    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) == 0:
            raise forms.ValidationError ('※本文を入力してください。')
        return text

    class Meta:
        model = Comment
        fields = ('author', 'text',)