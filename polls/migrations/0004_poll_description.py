# Generated by Django 5.1.7 on 2025-03-11 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_choice_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
