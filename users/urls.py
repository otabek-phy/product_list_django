from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from core import settings
from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_page, name='login_page' ),
    path('register/', views.register_page, name='register_page' ),
]