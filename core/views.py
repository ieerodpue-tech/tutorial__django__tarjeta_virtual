from django.shortcuts import render, HttpResponse

html_base = """ 
<h1> WEB </h1>
<ul>
    <li><a href="/">portada</a></li>
    <li><a href="/about-me/">Acerca de </a></li>
    <li><a href="/portafolio/">portafolio</a></li>
    <li><a href="/contacto/">contacto</a></li>
</ul>
"""

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")


def portafolio(request):
    return render(request, "core/portafolio.html")
    
    


def contacto(request):
    return render(request, "core/contacto.html")
    
