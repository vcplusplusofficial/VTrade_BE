from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import CustomUserSerializer


def login_view(request):
    # Example content for a login view
    return HttpResponse("This is the login view.")


@api_view(['GET'])
def get_users(request):
    users = CustomUser.objects.all()
    serializer = CustomUserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])  # Only authenticated users can access this view
def update_profile(request):
    """
    Allows authenticated users to view or update their profile.
    """
    if request.method == 'GET':
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Update user profile with additional fields
        serializer = CustomUserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
