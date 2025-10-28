from django.db import models

# Create your models here.
class Usuarios(models.Model):

    class Meta:
        managed = False
        db_table = 'usuarios'