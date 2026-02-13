"""
URL configuration for tienda_videojuegos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #Aquí enrutaremos con las APPs que componen la herramienta, siendo este documento de url el principal

    path('',include('home.urls')), # incluimos las URLs de home en la raíz
    path('catalogo/',include('catalogo.urls')),# incluimos las URLs de catálogos, por lo que en base, ya solo deberemos de llamar a la vista con el name que está en la urls de catalogo
    path('buscador/',include('buscador.urls')),
    path('usuarios/',include('usuarios.urls')),

]
