# Generated by Django 5.1.7 on 2025-03-12 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_poll_down_vote_poll_up_vote_delete_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='down_vote',
            field=models.IntegerField(default=0),
        ),
    ]
