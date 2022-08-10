from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "layout.html")

def contacto(request, **kwargs):
    return render(request, "contact.html")

def principal(request):
    return render(request, "principal.html")

def contacto(request, **kwargs):
    return render(request, "contacto.html")

