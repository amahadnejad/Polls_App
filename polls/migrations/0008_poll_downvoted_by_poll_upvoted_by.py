# Generated by Django 5.1.7 on 2025-03-12 12:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_alter_poll_down_vote'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='downvoted_by',
            field=models.ManyToManyField(blank=True, related_name='downvoted_polls', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='poll',
            name='upvoted_by',
            field=models.ManyToManyField(blank=True, related_name='upvoted_polls', to=settings.AUTH_USER_MODEL),
        ),
    ]
