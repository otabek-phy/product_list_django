from django.shortcuts import render, redirect




def login_page(request):
    return render(request, 'users/login.html')




def register_page(request):
    return render(request,'users/register.html')




def logout_page(request):
    return render()
pass