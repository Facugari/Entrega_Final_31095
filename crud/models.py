from django.db import models

class Usuario(models.Model):
    
    nombre = models.CharField(primary_key=True, max_length=20)
    mail = models.EmailField(max_length=20)
    consulta = models.CharField(max_length=500)
    