from django.shortcuts import render, redirect
from django.http import Http404

from .models import Poll
from django.contrib.auth.decorators import login_required


def poll_list_view(request):
    polls = Poll.objects.all()
    return render(request, 'polls/polls_list.html', context={
        'polls': polls,
    })


def poll_detail_view(request, pk):
    poll = Poll.objects.get(pk=pk)

    return render(request, 'polls/poll_detail.html', context={
        'poll': poll,
    })
