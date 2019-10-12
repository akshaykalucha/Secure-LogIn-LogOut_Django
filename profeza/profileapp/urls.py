from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LoginView

app_name = 'profileapp'



urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.register, name='register'),
    path('home/', views.home, name='home'),
]