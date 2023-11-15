from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('success/<int:title>/', views.success_login, name='success_login'),
    path('login_captcha', views.login_captcha, name='login_captcha')

    # Add more URL patterns for your app as needed
]
