from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_screen, name="home_screen"),
    path('posts/<int:id>', views.show_post, name = "post_show"),
    path('create/', views.create_post, name = "create_post")
]