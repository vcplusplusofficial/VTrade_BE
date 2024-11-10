from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('users/', views.UserListCreateView.as_view(), name='user-list-create'),  # List all users, create a user
    path('users/<slug:slug>-<uuid:id>/', views.UserDetailView.as_view(), name='user-detail'),  # Retrieve, update, delete by ID
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),

    # path('users/', views.get_users, name='get-user'),
    # path('users/register/', views.create_user, name='user-register'),
    # path('users/profile/', views.update_profile, name='user-profile'),
    # path('users/<int:id>/', views.user_detail, name='user-detail'),
]
