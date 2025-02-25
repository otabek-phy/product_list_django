from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
        path('home/', views.index, name='index'),
        path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
]