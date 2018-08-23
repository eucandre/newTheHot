#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import uuid

DURACAO = ((u'Um Dia', 'Um Dia'), (u'Uma Semana', 'Uma Semana'), (u'15 Dias', '15 Dias'), (u'Um Mes', 'Um Mes'),
           (u'Tres Meses', 'Tres Meses'), (u'Seis Meses', 'Seis Meses'), (u'Um Ano', 'Um Ano'))

ESTADOS = [ ('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA','Maranhão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'),
            ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
            ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')]


class ClienteAnuncio(models.Model):
    # cliente = models.ForeignKey('gestao.Usuario')
    cliente = models.ForeignKey(User)
    valor = models.FloatField(null=False)
    fotos = models.FileField(upload_to='fotos/%Y/%m/%d/')
    videos = models.FileField(upload_to='videos/%Y/%m/%d/', blank=True)
    auditoria = models.BooleanField(default=False)
    ativo = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.cliente.__str__()



class Motel(models.Model):
    id         = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #dono       = models.ForeignKey('gestao.Usuario')
    nome       = models.CharField(max_length=10)
    fotos      = models.FileField(upload_to='fotos/%Y/%m/%d/', blank=True)
    descricao  = models.CharField(max_length=200)
    estrelas   = models.IntegerField(choices=[(1, 'Uma'), (2, 'Duas'), (3, 'Três'), (4, 'Quatro'), (5, 'Cinco')])
    endereco   = models.CharField(max_length=200)
    telefone   = models.CharField(max_length=15)
    bairro     = models.CharField(max_length=25)
    cidade     = models.CharField(max_length=70)
    estado     = models.CharField(max_length=2, choices=ESTADOS)
    latitude   = models.DecimalField(max_digits=9, decimal_places=6)
    longitude  = models.DecimalField(max_digits=9, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Quarto(models.Model):
    motel     = models.ForeignKey('Motel')
    fotos     = models.FileField(upload_to='fotos/%Y/%m/%d/', blank=True)
    descricao = models.CharField(max_length=100)
    tipo      = models.CharField(max_length=10)
    preco     = models.FloatField()
    ocupado   = models.BooleanField()


