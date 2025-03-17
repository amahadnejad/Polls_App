from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Poll, Comment

User = get_user_model()

# Customize Django Admin Titles
admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to the Pollster Admin Area"


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'datetime_created', 'user', 'up_vote', 'down_vote')
    search_fields = ('question',)
    readonly_fields = ('datetime_created',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'poll', 'body', 'datetime_created', 'is_active')