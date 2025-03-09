from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Poll, Choice

User = get_user_model()


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'user', 'datetime_created')
    search_fields = ('question',)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('poll', 'user', 'choice_text', 'votes')
    search_fields = ('choice_text',)
