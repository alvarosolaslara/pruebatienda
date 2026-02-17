from django.contrib import admin
from .models import Juego

admin.site.register(Juego)

# Aquí indicaremos a Django que desde admin queremos gestionar la app, en este caso sería catálogo