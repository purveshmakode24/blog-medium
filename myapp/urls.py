from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('<username>/add_posts/', views.add_posts, name='add_posts'),
    path('add_posts_submit/', views.add_posts_submit, name='add_posts_submit'),
    path('<username>/delete_posts/<int:pid>/', views.delete_posts, name='delete_posts'),
    path('<username>/update_post/<int:pid>/', views.update_post, name='update_post'),
    path('full_post/<int:pid>/<slug>/', views.full_post, name='full_post'),
    path('like/<int:pid>/<slug>/', views.like, name='like'),
    path('dislike/<int:pid>/<slug>/', views.dislike, name='dislike'),
    path('profile/<username>/my_liked_posts/', views.my_liked_posts, name='my_liked_posts'),
    path('error_404/', views.error_404, name='error_404'),
]
