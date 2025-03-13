from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)  # Email bo‘yicha foydalanuvchini topamiz
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")  # Muvaffaqiyatli login bo‘lsa, home sahifasiga yo‘naltiramiz
            else:
                messages.error(request, "Email yoki parol noto‘g‘ri!")
        except User.DoesNotExist:
            messages.error(request, "Bunday email mavjud emas!")

    return render(request, "users/login.html")




def register_page(request):
    return render(request,'users/register.html')




def logout_page(request):
    pass