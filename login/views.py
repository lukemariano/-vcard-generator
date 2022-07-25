# from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

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


def vcard(request):
    return render(request, 'login/vcard.html')
