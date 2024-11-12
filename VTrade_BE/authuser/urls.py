from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('/', views.UserListCreateView.as_view(), name='user-list-create'),
    path('/<slug:slug>-<uuid:id>/', views.UserDetailView.as_view(), name='user-detail'),
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),
]