from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('add_posts', views.add_posts, name='add_posts'),
    path('add_posts_submit', views.add_posts_submit, name='add_posts_submit'),
    path('delete_posts', views.delete_posts, name='delete_posts'),
]
