from django.urls import path
from .views import *

urlpatterns = [
    
    path('', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('dashboard', dashboard, name='dashboard'),
    path('ChangePassword', ChangePassword, name='ChangePassword'),
    path('UserProfilePicture', UserProfilePicture, name='UserProfilePicture'),
    
]