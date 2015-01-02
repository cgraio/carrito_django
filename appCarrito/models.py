from django.db import models

# Create your models here.

class Pieza(models.Model):
	codigo = models.IntegerField()
	descripcion = models.CharField(max_length=200)

class Vendedor(models.Model):
	nombre = models.CharField(max_length=200)

class Publicacion(models.Model):
	vendedor = models.ForeignKey(Vendedor)
	pieza = models.ForeignKey(Pieza)
	fecha_publicada = models.DateTimeField('date_published')
