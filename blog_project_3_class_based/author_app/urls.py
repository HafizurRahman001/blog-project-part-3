from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    # path('user_login/', views.user_login, name='user_login'),
    path('user_login/', views.UserLogIn.as_view(), name='user_login'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/password_change/', views.password_change, name='password_change'),
    path('user_logout', views.user_logout, name='user_logout'),
]