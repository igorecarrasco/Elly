from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Elly(models.Model):
	title = models.TextField()
	tags = models.TextField()
	pubdate = models.DateTimeField()
	link = models.TextField()
	thumb = models.TextField()
	author = models.TextField()
	section = models.TextField()
	socialhed = models.TextField(default="")
	# def __str__(self):
 #    	return self.title