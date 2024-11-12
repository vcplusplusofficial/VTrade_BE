from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CustomUser
from .serializers import CustomUserSerializer


# View for listing all users and creating new users
class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]


# View for retrieving, updating, and deleting a specific user by ID
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'id'

    def get_object(self):
        # Custom method to handle 404 if user is not found
        try:
            return CustomUser.objects.get(id=self.kwargs['id'])
        except CustomUser.DoesNotExist:
            raise NotFound("User not found.")


# View for retrieving and updating the profile of the currently logged-in user
class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Returns the currently logged-in user based on the request context
        return self.request.user


# Custom view to filter users by first name or return all users
class CustomUserList(APIView):
    def get(self, request, format=None):
        name = request.query_params.get("first_name")

        if name:
            users = CustomUser.objects.filter(first_name=name)
        else:
            users = CustomUser.objects.all()

        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Basic login view for non-REST login (just a placeholder example here)
def login_view(request):
    return HttpResponse("This is the login view.")
