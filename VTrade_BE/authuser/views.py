from django.shortcuts import render
from django.http import HttpResponse


def login_view(request):
    # Example content for a login view
    return HttpResponse("This is the login view.")
