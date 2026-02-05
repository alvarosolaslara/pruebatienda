from django.urls import path
from.import views #importamos la vistas views.py

urlpatterns = [
    #con la ruta vacía '', indicamos que sea la ruta raiz
    path('',views.index, name='home'), #ruta principal: llama a la vista index, ten en cuenta que antes se deberá de tener creada la vista en views
    path('contacto', views.contacto, name='contacto'), #ruta contacto: llama a la ruta, ten en cuenta que antes se deberá de tener creada la vista en views
]
