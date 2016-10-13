from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Tweet(models.Model):
    twitid = models.CharField(max_length=30)
    texto = models.TextField()
    def __str__(self):
    	return self.texto
