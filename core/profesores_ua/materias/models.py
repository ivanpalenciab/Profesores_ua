from django.db import models

class Materia(models.Model):
    nombre = models.CharField(max_length=120)
    semestre = models.IntegerField() 
    carrera = models.CharField(max_length=120)
