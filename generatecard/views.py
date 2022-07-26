from django.shortcuts import render

# Create your views here.


def vcard_index(request):
    return render(request, 'generatecard/vcard.html')


def vcard_form(request):
    pass
