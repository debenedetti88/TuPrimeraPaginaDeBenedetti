from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    genero = models.CharField(max_length=20)


class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)
    

class Editorial(models.Model):
    nombre = models.CharField(max_length=50)
    sitio_web = models.CharField(max_length=50)