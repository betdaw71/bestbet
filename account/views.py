from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.conf import settings
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import send_mail
from events.models import Bet


@login_required
def home(request):
    return render(request, 'account/home.html')

def change_username(request,username):
    if request.user.is_authentificated:
        user = User.objects.get(id=request.user.id)
        user.username = username
        user.save()
        return redirect('home')
    else:
        return redirect('login')
def history(request):
    user = User.objects.get(id=request.user.id)
    events = Bet.objects.filter(user=user)
    data={'bets':events}
    return render(request,'account/history.html',context=data)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Ваш пароль был успешно изменен!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {
        'form': form
    })

def identify(request):
    return render(request,'account/identify.html')

def edit(request,id):
    try:
        user = User.objects.get(id=id)

        if request.method == "POST":
            user.number = request.POST.get("number")
            user.email = request.POST.get("email")
            user.location = request.POST.get("location")
            user.first_name = request.POST.get("name")
            messages.success(request, 'Иформация о вас была успешно изменена!')
            user.save()
            return redirect("home")
        else:
            return render(request, "account/home.html")
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                email = form.cleaned_data.get('email')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(email=email, password=raw_password)
                login(request, user)
                return redirect('home')
            except:
                messages.error(request,'Ошибка при ригестрации')
                return render(request, 'account/signup.html', {'form': form})
        else:
            messages.error(request,'Ошибка при ригестрации')
            return render(request, 'account/signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})


def number_change(request,id):
    user = User.objects.get(id = id)
    if request.method == 'POST':
        user.number = request.POST.get('number')
        user.save()
        messages.success(request, 'Иформация о вас была успешно изменена!')
        return redirect('home')
    return render(request,'account/number_change.html')

# send_mail('Подтверждение почты','Test111','babayan.dawid2016@gmail.com',['babayan.dawid2017@yandex.ru'],fail_silently=False,)

def signup_activate(request,id):
    user = User.objects.get(id=id)
    current_site = get_current_site(request)
    subject = 'Activate Your MySite Account'
    message = render_to_string('account/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
    })
    # user.email_user(subject, message)
    print(message)
    print(user.email)
    print('asdasdsa')
    send_mail(
            'Подтверждение почты',
            message,
            'babayan.dawid2016@gmail.com',
            [user.email],
            fail_silently=False,
        )
    return redirect('account_activation_sent')



def account_activation_sent(request):
    return render(request, 'account/account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.email_confirm = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account/account_activation_invalid.html')
