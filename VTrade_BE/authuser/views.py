from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import CustomUser
from .serializers import CustomUserSerializer

def login_view(request):
    # Example content for a login view
    return HttpResponse("This is the login view.")
