from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.index, name="home"),
    path('users/new/', views.new, name="new_user_form"),
    path('users/<int:user_id>/edit/', views.edit, name="edit_user_form"),
    path('users/<int:user_id>/', views.display, name="display_user"),
    path('users/create/', views.create, name="create_user"),
    path('users/<int:user_id>/destroy/', views.delete, name="destroy_user"),
    path('users/update/', views.update, name="update_user")
]