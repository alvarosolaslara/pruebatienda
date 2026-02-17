from django.db import models


# Utilizaremos los modelos para crear una tabla dentro de la base de datos, en este caso tendremos la tabla juego con sus atributos
class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    plataforma = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200, default="default.png") # con maxleng alamcenaremos el nombre del juego y en default en caso de que no localice imagen que coloque una por defecto

    def __str__(self):
        return self.nombre
    









# CADA VEZ QUE SE HAGAN CAMBIOS, MODIFICACIONES O CREACIONES EN EL MODELO SE DEBERÁ DE REALIZAR MIGRACIONES
# python manage.py makemigrations
# python manage.py migrate