from django.db import models
from django.contrib.auth import get_user_model


class Poll(models.Model):
    question = models.CharField(max_length=700)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class Choice(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, blank=True)
    votes = models.IntegerField(default=0)
