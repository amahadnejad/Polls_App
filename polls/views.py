from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Poll
from .forms import PollForm


def poll_list_view(request):
    polls = Poll.objects.all()
    return render(request, 'polls/polls_list.html', context={'polls': polls})


def poll_detail_view(request, pk):
    poll = Poll.objects.get(pk=pk)
    return render(request, 'polls/poll_detail.html', context={'poll': poll})


@login_required
def up_vote(request, pk):
    poll = get_object_or_404(Poll, pk=pk)

    if request.user in poll.downvoted_by.all():
        poll.down_vote -= 1
        poll.up_vote += 1
        poll.downvoted_by.remove(request.user)
        poll.upvoted_by.add(request.user)
    elif request.user not in poll.upvoted_by.all():
        poll.up_vote += 1
        poll.upvoted_by.add(request.user)

    poll.save()
    return redirect('poll_detail', pk=pk)


@login_required
def poll_create_view(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            poll = form.save(commit=False)
            poll.user = request.user
            poll.save()
            return redirect(poll.get_absolute_url())
    else:
        form = PollForm()

    return render(request, 'polls/poll_create.html', {'form': form})


@login_required
def down_vote(request, pk):
    poll = get_object_or_404(Poll, pk=pk)

    if request.user in poll.upvoted_by.all():
        poll.up_vote -= 1
        poll.down_vote += 1
        poll.upvoted_by.remove(request.user)
        poll.downvoted_by.add(request.user)
    elif request.user not in poll.downvoted_by.all():
        poll.down_vote += 1
        poll.downvoted_by.add(request.user)

    poll.save()
    return redirect('poll_detail', pk=pk)


def poll_update_view(request, pk):
    poll = get_object_or_404(Poll, pk=pk)

    if request.method == "POST":
        form = PollForm(request.POST, instance=poll)
        if form.is_valid():
            form.save()
            return redirect("poll_detail", pk=poll.pk)
    else:
        form = PollForm(instance=poll)

    return render(request, "polls/poll_update.html", {
        "form": form,
        'poll': poll,
    })


def poll_delete_view(request, pk):
    poll = get_object_or_404(Poll, pk=pk)

    if request.method == "POST":
        poll.delete()
        return redirect("polls_list")

    return render(request, "polls/poll_delete.html", {"poll": poll})
