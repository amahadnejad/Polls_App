from django.urls import path

from .views import poll_list_view, poll_detail_view

urlpatterns = [
    path('', poll_list_view, name='polls_list'),
    path('poll/<int:pk>/', poll_detail_view, name='poll_detail'),
]
