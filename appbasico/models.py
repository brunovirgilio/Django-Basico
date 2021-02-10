from django.db import models
import struct
import zlib

class Equipe(models.Model):
    nome         = models.CharField(max_length=250)
    fundacao     = models.CharField(max_length=5)
    carioca      = models.CharField(max_length=3)
    brasileiro   = models.CharField(max_length=3)
    copadobrasil = models.CharField(max_length=3)
    sulamericana = models.CharField(max_length=3, default="")
    libertadores = models.CharField(max_length=3)
    mundial      = models.CharField(max_length=3, default="")
    imagem       = models.ImageField(upload_to="media")

    def __str__(self):
        return self.nome




