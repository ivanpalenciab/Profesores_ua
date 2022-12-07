from django.db import models
from materias.models import Materia
from profesores.models import Profesor

class Curso(models.Model):
    materia_id = models.ForeignKey(Materia, on_delete=models.CASCADE)
    grupo = models.IntegerField()
    profesor_id = models.ForeignKey(Profesor, on_delete=models.SET_NULL,null=True)
