from django.db import models
import struct
import zlib

from django.db.models import signals
from django.template.defaultfilters import slugify

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

class Base(models.Model):
    criado     = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo      = models.BooleanField('Ativo7', default=True)

    class Meta:
        abstract = True

class Postagem(Base):
    nome = models.CharField(max_length=100, default="")	
    post = models.CharField(max_length=140, default="")
	
    def __str__(self):
        return self.nome