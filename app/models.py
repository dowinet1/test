from django.db import models
from django.contrib.auth.models import User, AbstractUser
import json

# Create your models here.

TIPOS_USUARIO = (
	('Jefactura ISC','Jefactura ISC'),
	('Secretaria','Secretaria'),
    ('Jefactura de Docencia', 'Jefactura de Docencia'),
    ('Jefactura de Vinculacion', 'Jefactura de Vinculacion'),
    ('Jefactura de Investigacion', 'Jefactura de Investigacion'),
    ('Jefactura de Laboratorio', 'Jefactura de Laboratorio'),
    ('Docentes', 'Docentes'),
)

class Usuarios(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100, choices=TIPOS_USUARIO)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.usuario.username
