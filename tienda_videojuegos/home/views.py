from django.shortcuts import render

# Vista de la página principal request=solicitud
def index(request):
    #rendex toma el request y el archivo HTML que queramos mostrar
    return render(request, 'home/index.html')

# Vista de la página de contacto
def contacto(request):
    return render(request, 'home/contacto.html')
