from .views import SignUpView, UsersListView
from django.urls import path, include

app_name = 'users'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('users/', UsersListView.as_view(), name='users_list'),
]