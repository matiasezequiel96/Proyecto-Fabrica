from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    nombre_pieza = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    numero_molde = models.CharField(max_length=50)

    def __str__(self):
        return(f"{self.nombre_pieza}")
