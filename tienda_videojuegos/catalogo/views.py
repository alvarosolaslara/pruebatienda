from django.shortcuts import render
from django.core.paginator import Paginator
from catalogo.models import Juego

def lista_juegos(request):

    #Engancharemos con la base de datos, le solicitaremos que nos den todos los elementos y que los ordenen por id
    juegos = Juego.objects.all().order_by('id')

    #Indicaremos que que mostraremos x juegos por página
    paginator = Paginator(juegos, 6)

    #Obtendremos el número de página desde la URL(?pager=2)
    page_number = request.GET.get('page')

    #Obtendremos los objetos de esa página
    page_obj = paginator.get_page(page_number)

    #Pasamos la paginación a la página
    contexto_catalogo_juegos = {'lista_juegos':page_obj} #introduciremos el valor del dicionario en la variable
    return render(request, 'catalogo/lista_juegos.html', contexto_catalogo_juegos) # Pasaremos el valor del diccionario al html correspondiente


