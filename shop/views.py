from django.db.models import Q
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from shop.models import Product, Category
from shop.forms import ProductModelForm, CommentModelForm


# Create your views here.


def index(request):
    search_query = request.GET.get('q', '')
    products = Product.objects.all().order_by('-updated_at')
    categories = Category.objects.all()
    if search_query:
        products = Product.objects.filter(Q(name__icontains=search_query)|Q(description__icontains=search_query))
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
#     return render(request, 'shop/product-create.html', context)



@login_required(login_url='/admin/')
def product_create(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')


    context = {
        'form': form,
        'action': 'Create'
    }
    return render(request, 'shop/product-create.html', context)


@login_required(login_url='/admin/')
def product_update(request, product_id):
    product = get_object_or_404(Product,id=product_id)
    form = ProductModelForm(instance=product)
    if request.method == "POST":
        form = ProductModelForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id)
    context = {
        "product": product,
        "form": form,
        'action': 'Update'
    }
    return render(request, 'shop/product-update.html', context)




@login_required(login_url='/admin/')
def product_delete(request, product_id):
    product = Product.objects.get(id=product_id)
    if product:
        product.delete()
        return redirect('index')
    return render(request, 'shop/detail.html', {'product': product})


def comment_view(request, pk):
    product = Product.objects.get(id=pk)
    form = CommentModelForm()
    if request.method == "POST":
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            rating = request.POST.get('rating')
            print(type(rating))
            comment.rating = rating
            comment.product = product
            comment.save()
            return redirect('product_detail', product.id)


    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'shop/detail.html', context)