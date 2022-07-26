# from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import UserRegistrationForm

# Create your views here.


def index(request):
    return render(request, 'login/index.html')


def login_view(request):
    return render(request, 'login/login.html')


def login_auth(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login.vcard')
        else:
            return render(request, 'login/login.html', {
                'message': "Invalid Credentials",
            })


def logout_view(request):
    logout(request)
    return redirect('login.index')


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(
                request, f'Your account has been created. You can log in now!')
            return redirect('login.login_view')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'login/register.html', context)


def vcard(request):
    return render(request, 'login/vcard.html')
