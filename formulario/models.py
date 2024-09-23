# formulario/models.py
from django.db import models

class RegistroMaterial(models.Model):
    material = models.CharField(max_length=100)
    cantidad = models.IntegerField()

    def __str__(self):
        return f'{self.material} - {self.cantidad}'
