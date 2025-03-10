from django.shortcuts import render

from .models import Poll


def poll_list_view(request):
    polls = Poll.objects.all()
    return render(request, 'polls/polls_list.html', context={
        'polls': polls,
    })





def poll_vote(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)

    if request.method == 'POST':
        vote = request.POST.get(f'vote_{poll.id}')

        if vote == 'agree':
            choice_text = 'Agree'
        elif vote == 'not_agree':
            choice_text = 'Not Agree'
        else:
            return HttpResponse('Invalid vote', status=400)

        # Create or update the user's vote
        if Choice.objects.filter(user=request.user, poll=poll).exists():
            choice = Choice.objects.get(user=request.user, poll=poll)
            choice.choice_text = choice_text
            choice.save()
        else:
            Choice.objects.create(user=request.user, poll=poll, choice_text=choice_text)

        return redirect('poll_list')  # Redirect back to the poll list page

    return HttpResponse('Invalid method', status=405)