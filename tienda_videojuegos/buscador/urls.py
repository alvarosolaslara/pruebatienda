from django.urls import path
from.import views #importamos la vistas views.py
#aunque no tengamos ninguna url definida será obligatorio tener urlpatterns, aunque sea bacía
urlpatterns = [ 
    path('',views.buscar_juegos, name='buscador_juegos'),
    
]