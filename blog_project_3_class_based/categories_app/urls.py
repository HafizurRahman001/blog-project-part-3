from django.urls import path
from . import views

urlpatterns = [
    path('add_categories/', views.add_categories, name='add_categories'),
]