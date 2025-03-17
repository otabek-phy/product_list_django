from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def login_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user_auth = authenticate(request, username=user.username, password=password)
            if user_auth is not None:
                login(request, user_auth)
                return redirect('home')
            else:
                messages.error(request, "Email yoki parol noto'g'ri!")
        except User.DoesNotExist:
            messages.error(request, "Bunday email mavjud emas!")

    return render(request, 'users/login.html')

def register_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Bu username allaqachon band!")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Bu email allaqachon ishlatilgan!")
        elif password != password2:
            messages.error(request, "Parollar mos emas!")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Muvaffaqiyatli ro'yxatdan o'tdingiz! Login qiling.")
            return redirect('login')

    return render(request, 'users/register.html')

def logout_page(request):
    logout(request)
    messages.success(request, "Tizimdan muvaffaqiyatli chiqdingiz!")
    return redirect('login')
