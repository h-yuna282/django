from django.db import models

# Create your models here.
class Libro(models.model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    isbn = models.CharField(max_length=45)