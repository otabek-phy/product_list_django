from django.shortcuts import render, get_object_or_404

from shop.models import Product, Category


# Create your views here.


def index(request):
    products = Product.objects.all().order_by('-updated_at')
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'shop/home.html', context)


def product_detail(request,product_id):
    product = get_object_or_404(Product,id=product_id)
    context = {
    "product": product,
    }
    return render(request, 'shop/detail.html',context)

def category_detail(request,category):
    products = Product.objects.all().filter(category=category)
    categories = Category.objects.all()
    context = {
        "categories": categories,
        "products": products,
    }
    return render(request, 'shop/home.html',context)



def add_comment():
    pass