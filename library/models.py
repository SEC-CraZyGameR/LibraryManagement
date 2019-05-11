from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Book(models.Model):
	bookname = models.CharField(max_length = 100)
	authorname = models.CharField(max_length = 100)
	edition = models.CharField(max_length = 50)
	description = models.TextField(default='')

	def __str__(self):
	    return self.bookname
