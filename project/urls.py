"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from myapp import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('users/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('users/logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('users/register/', views.register, name='register'),
    path('users/password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),
         name='password_reset'),
    path('users/password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('users/password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('users/password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
    path('profile/<username>/', views.profile, name='profile'),
]
