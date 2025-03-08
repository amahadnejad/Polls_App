from django.urls import path

from .views import poll_list_view

urlpatterns = [
    path('', poll_list_view, name='polls_list'),
]
