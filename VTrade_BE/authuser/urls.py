from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('users/', views.get_users, name='get-user'),
    path('users/register/', views.create_user, name='user-register'),
    path('users/profile/', views.update_profile, name='user-profile'),
]
