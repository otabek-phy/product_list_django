from pydoc import describe

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from shop.models import Product, Category
from shop.forms import ProductForm


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


# @login_required(login_url='/admin/')
# def product_create(request):
#     form = ProductModelForm()
#     if request.method == 'POST':
#         form = ProductModelForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#     context = {
#         'form': form
#     }
#     return render(request, 'shop/add-product.html', context)



@login_required(login_url='/admin/')
def product_create(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')


    context = {
        'form': form
    }
    return render(request, 'shop/add-product.html', context)




def product_delete(request, pk):
    try:
        product = Product.objects.get(id=pk)
        product.delete()
        return redirect('index')
    except Product.DoesNotExist as e:
        print(e)