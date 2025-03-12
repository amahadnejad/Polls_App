from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Poll


def poll_list_view(request):
    polls = Poll.objects.all()
    return render(request, 'polls/polls_list.html', context={'polls': polls})


def poll_detail_view(request, pk):
    poll = Poll.objects.get(pk=pk)
    return render(request, 'polls/poll_detail.html', context={'poll': poll})


@login_required
def up_vote(request, pk):
    poll = Poll.objects.get(pk=pk)

    if request.user in poll.downvoted_by.all():
        # If the user had downvoted, remove downvote and add upvote
        poll.down_vote -= 1
        poll.up_vote += 1
        poll.downvoted_by.remove(request.user)
        poll.upvoted_by.add(request.user)
    elif request.user not in poll.upvoted_by.all():
        # If the user hasn't voted before or is changing from no vote
        poll.up_vote += 1
        poll.upvoted_by.add(request.user)

    poll.save()
    return redirect('poll_detail', pk=pk)


@login_required
def down_vote(request, pk):
    poll = Poll.objects.get(pk=pk)

    if request.user in poll.upvoted_by.all():
        # If the user had upvoted, remove upvote and add downvote
        poll.up_vote -= 1
        poll.down_vote += 1
        poll.upvoted_by.remove(request.user)
        poll.downvoted_by.add(request.user)
    elif request.user not in poll.downvoted_by.all():
        # If the user hasn't voted before or is changing from no vote
        poll.down_vote += 1
        poll.downvoted_by.add(request.user)

    poll.save()
    return redirect('poll_detail', pk=pk)
