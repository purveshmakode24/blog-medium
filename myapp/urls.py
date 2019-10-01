from django.urls import path
from myapp.views import FullPostView

from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('<username>/add_posts/', views.add_posts, name='add_posts'),
    path('add_posts_submit/', views.add_posts_submit, name='add_posts_submit'),
    path('<username>/delete_posts/', views.delete_posts, name='delete_posts'),
    path('<username>/update_post/', views.update_post, name='update_post'),
    # path('full_post/<int:pid>/<slug>/', views.full_post, name='full_post'),
    path('full_post/<int:pid>/<slug>/', FullPostView.as_view(), name='full_post'),
    path('error_404/', views.error_404, name='error_404'),
]
