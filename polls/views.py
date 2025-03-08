from django.shortcuts import render
from django.http import HttpResponse


def poll_list_view(request):
    return HttpResponse("Hello World")
