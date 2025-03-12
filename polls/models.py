from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Poll(models.Model):
    question = models.CharField(max_length=700)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    description = models.TextField(blank=True)

    up_vote = models.PositiveIntegerField(default=0)
    down_vote = models.PositiveIntegerField(default=0)

    upvoted_by = models.ManyToManyField(get_user_model(), related_name='upvoted_polls', blank=True)
    downvoted_by = models.ManyToManyField(get_user_model(), related_name='downvoted_polls', blank=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('poll_detail', args=[self.id])

    def __str__(self):
        return self.question
