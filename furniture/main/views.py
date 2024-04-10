from django.shortcuts import render

def index(request):
    return render(request, 'main/main.html')


def contacts(request):
    return render(request, 'main/phone.html')