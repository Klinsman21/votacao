from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

now = datetime.now()
other_time = now + timedelta(hours=1)


class Votacao(models.Model):

  name = models.CharField(max_length=150, verbose_name='nome')
  description = models.TextField(verbose_name='descrição')
  resultado = models.BooleanField(default=False, verbose_name='resultado')
  votoSim = models.PositiveIntegerField(validators=[MinValueValidator(0)], verbose_name='votosim', default=0)
  votoNao = models.PositiveIntegerField(validators=[MinValueValidator(0)], verbose_name='votonao', default=0)
  final_time = models.TimeField(verbose_name='horario de final', default=other_time)
  active = models.BooleanField(default=True, verbose_name='ativado')

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'votação'
    verbose_name_plural = 'votações'

class Votadas(models.Model):

  userId = models.PositiveIntegerField(validators=[MinValueValidator(0)], verbose_name='id-user', default=0)
  leiId = models.PositiveIntegerField(validators=[MinValueValidator(0)], verbose_name='id-lei', default=0)
  def __str__(self):
    return str(self.leiId)
  
  class Meta:
    verbose_name = 'votado'
    verbose_name_plural = 'votadas'

class Comments(models.Model):
  comentario = models.TextField(verbose_name='comentario')
  leiId = models.PositiveIntegerField(validators=[MinValueValidator(0)], verbose_name='id-lei', default=0)
  def __str__(self):
    return "Comentario"
    
  class Meta:
    verbose_name = 'comentario'
    verbose_name_plural = 'comentarios'
 
# Create your models here.
