from django.db import models

class Profesor(models.Model):
    id = models.IntegerField(primary_key=True)
    primer_nombre = models.CharField(max_length=120)
    segundo_nombre = models.CharField(max_length=120, null=True)
    primer_apellido = models.CharField(max_length=120)
    segundo_apellido = models.CharField(max_length=120,null=True)
    calificacion = models,models.DecimalField( max_digits=4, decimal_places=2,default=0)

