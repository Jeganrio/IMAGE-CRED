from django.db import models

# models.py
class Hotel(models.Model):
	name = models.CharField(max_length=50)
	Img = models.ImageField(upload_to='images/')
