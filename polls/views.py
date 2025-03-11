from django.shortcuts import render

from .models import Poll


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
