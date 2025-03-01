from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
        path('home/', views.index, name='index'),
        path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
        path('home_category/<int:category>/',views.category_detail,name='home_category'),
        path('product-create/', views.product_create, name='product_create'),
]