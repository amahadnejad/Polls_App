# Generated by Django 5.0.2 on 2025-03-17 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
