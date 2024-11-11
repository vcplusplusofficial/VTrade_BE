from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework import permissions
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from .serializers import CustomUserSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'id'

    def get_object(self):
        try:
            return CustomUser.objects.get(id=self.kwargs['id'])
        except CustomUser.DoesNotExist:
            raise NotFound("User not found.")


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class CustomUserList(APIView):
    def get(self, request, format=None):
        name = request.query_params.get("first_name")

        if name:
            users = CustomUser.objects.filter(first_name=name)
        else:
            users = CustomUser.objects.all()

        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


def login_view(request):
    # Example content for a login view
    return HttpResponse("This is the login view.")
