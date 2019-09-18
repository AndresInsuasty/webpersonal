from django.shortcuts import render, HttpResponse

html_base = """
<h1>Mi web personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/">Acerca de</a></li>
    <li><a href="/portafolio/">Portafolio</a></li>
    <li><a href="/contacto/">Contacto</a></li>
</ul>
"""


# Create your views here.

def home(request):
    return HttpResponse(html_base+"""
    <h2>portada</h2>
    <p>Esta es la portada</p>
    """)


def about(request):
    return HttpResponse(html_base+"""
    <h2>Acerca de</h2>
    <p>Me llamo Andres y soy Ingeniero programador</p>
    """)


def portafolio(request):
    return HttpResponse(html_base+"""
    <h2>Portafolio</h2>
    <ul>
        <li>Programacion</li>
        <li>Desarrollo Web</li>
        <li>Inteligencia artificial</li>
    </ul>
    """)


def contacto(request):
    return HttpResponse(html_base+"""
    <h2>Contacto</h2>
    <p>Escribeme al correo andresinsuastyd10@gmail.com con tus inquietudes</p>
    """)
