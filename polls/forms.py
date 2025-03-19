from django import forms

from .models import Poll, Comment


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'description', 'cover']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'body']
