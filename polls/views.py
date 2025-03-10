from django.shortcuts import render


def poll_list_view(request):
    return render(request, 'polls/polls_list.html')
