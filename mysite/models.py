# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Simplex(models.Model):
    max_choice = "Max"
    min_choice = "Min"
    maxmin_choices = ((max_choice, "Max"),
                      (min_choice, "Min"))

    maior = ">="
    igual = "="
    menor = "<="
    maiormenor_choices = ((maior,">="),
                          (igual, "="),
                          (menor, "=>"))

    x1 = models.FloatField(max_length=10)
    x2 = models.FloatField()
    r1x1 = models.FloatField()
    r1x2 = models.FloatField()
    r2x1 = models.FloatField()
    r2x2 = models.FloatField()
    r3x1 = models.FloatField()
    r3x2 = models.FloatField()

    maxmin = models.CharField(choices=maxmin_choices, default=max_choice,
                              max_length=10)
    maiormenorR1 = models.CharField(choices=maiormenor_choices,
                                    default=maior, max_length=10)
    maiormenorR2 = models.CharField(choices=maiormenor_choices,
                                    default=maior,max_length=10)
    maiormenorR3 = models.CharField(choices=maiormenor_choices,
                                    default=maior,max_length=10)

    b1 = models.FloatField()
    b2 = models.FloatField()
    b3 = models.FloatField()

    def __str__(self):
        return "x1="+str(self.x1)+"; x2="+str(self.x2)


class Oferta(models.Model):
    O = models.FloatField()

    def __str__(self):
        return "O: "+str(self.x)


class Demanda(models.Model):
    D = models.FloatField()

    def __str__(self):
        return "D:"+str(self.rx)