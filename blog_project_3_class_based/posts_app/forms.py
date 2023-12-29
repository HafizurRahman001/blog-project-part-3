from django import forms
from posts_app.models import Post,Comments


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        exclude = ['author']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name','email','body']

        