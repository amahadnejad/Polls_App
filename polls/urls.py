from django.urls import path

from .views import poll_list_view, poll_detail_view, up_vote, down_vote

urlpatterns = [
    path('', poll_list_view, name='polls_list'),
    path('poll/<int:pk>/', poll_detail_view, name='poll_detail'),
    path('poll/<int:pk>/vote/', up_vote, name='poll_vote'),
    path('poll/<int:pk>/down_vote/', down_vote, name='poll_down_vote'),
]
