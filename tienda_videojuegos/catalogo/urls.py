from django.urls import path
from.import views #importamos la vistas views.py
#aunque no tengamos ninguna url definida será obligatorio tener urlpatterns, aunque sea bacía

app_name = 'catalogo'

urlpatterns = [ 
    path('',views.lista_juegos, name='lista_juegos'),
    path('<int:pk>/', views.detalle_juego, name='detalle_juego'),# Utilizaremos el primari key en modo int y se lo pasaremos a la url
    
]