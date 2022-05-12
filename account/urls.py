from django.urls import path
from django.contrib.auth.views import LogoutView #, PasswordChangeView
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterForm.as_view(), name='register'),
    path('profile/', Userprofile.as_view(), name='profile'),
    path('update/<int:pk>', UserUpdate.as_view(), name='user_update'),
    path('acount/', UserList.as_view(), name='user_list'),
    ]
