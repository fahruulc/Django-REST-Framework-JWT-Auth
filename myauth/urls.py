from django.urls import path
from .views import (
    UserListCreateView,
    UserRetrieveUpdateDestroyView,
    UserRegistrationView,
    UserLogoutView
)

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('regis/', UserRegistrationView.as_view(), name='user-regis'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(),
         name='user-retrieve-update-destroy'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
]
