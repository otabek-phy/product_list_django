from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
        path('home/', views.index, name='index'),
        path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
        path('home_category/<int:category>/',views.category_detail,name='home_category'),
        path('product-create/', views.product_create, name='product_create'),
        path('product-delete/<int:product_id>/', views.product_delete, name='product_delete'),
        path('product-update/<int:product_id>/', views.product_update, name='product_update'),
        path('comment-view/<int:pk>/', views.comment_view, name='comment_view'),
]