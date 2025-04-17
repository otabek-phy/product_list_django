<<<<<<< HEAD
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from .models import CustomUser
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib import messages
from users.forms import LoginForm, RegisterModelForm


# Create your views here.


def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('shop:index')
                else:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        'Disabled account'
                    )
                    return render(request, 'users/login.html')
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Username or Password invalid'
                )
                return render(request, 'users/login.html')

    return render(request, 'users/login.html', {'form': form})


def register_page(request):
    form = RegisterModelForm()
    if request.method == 'POST':
        form = RegisterModelForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.is_superuser = True
            user.set_password(user.password)
            user.save()
            send_mail(
                'Hello Dear!',
                'You Successfully registered',
                'jasurmavlonov24@gmail.com',
                [user.email],
                fail_silently=False
            )
            login(request, user)
            return redirect('shop:index')
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)
=======
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
>>>>>>> bec937dddbf6a56e72c19afbac1753913be1532a

    return render(request, 'users/register.html')

def logout_page(request):
<<<<<<< HEAD
    if request.method == 'POST':
        logout(request)
        return redirect('shop:index')


class RegisterPage(FormView):
    template_name = 'users/register.html'
    form_class = RegisterModelForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = False
        user.set_password(user.password)
        user.save()
        current_site = get_current_site(self.request)
        subject = "Verify Email"
        message = render_to_string('users/email/verify_email_message.html', {
            'request': self.request,
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        user.save()
        email = EmailMessage(
            subject, message, to=[user.email]
        )
        email.content_subtype = 'html'
        email.send()
        return redirect('users:verify_email_done')




def email_required(request):
    if request.method == "POST":
        email = request.POST.get("email")
        user = request.user

        if user.is_authenticated and not user.email:
            user.email = email
            user.save()
            return redirect("shop:index")  # Asosiy sahifaga yo‘naltirish

    return render(request, "users/github/email-required.html")


def verify_email_done(request):
    return render(request, "users/email/verify_email_done.html")


def verify_email_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        messages.success(request, 'Your email has been verified.')
        return redirect('shop:index')
    else:
        messages.warning(request, 'The link is invalid.')
    return render(request, 'users/email/verify_email_confirm.html')
=======
    logout(request)
    messages.success(request, "Tizimdan muvaffaqiyatli chiqdingiz!")
    return redirect('login')
>>>>>>> bec937dddbf6a56e72c19afbac1753913be1532a
