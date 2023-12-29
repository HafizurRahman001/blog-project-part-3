from django.urls import path
from . import views

urlpatterns = [
    # path('add_post/', views.add_post, name='add_post'),
    path('add_post/', views.AddPostCreateView.as_view(), name='add_post'),
    # path('edit_post/<int:id>', views.edit_post, name='edit_post'),
    path('edit_post/<int:id>/', views.EditPost.as_view(), name='edit_post'),
    # path('delete_post/<int:id>/', views.delete_post, name='delete_post'),
    path('delete_post/<int:id>', views.DeletePost.as_view(), name='delete_post'),
    path('details/<int:id>', views.DetailsPost.as_view(), name='details'),
]