from django.db import models
from django.contrib.auth import get_user_model


class Poll(models.Model):
    question = models.CharField(max_length=700)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)



