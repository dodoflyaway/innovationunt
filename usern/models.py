from django.db import models
from django.contrib.auth.models import User


class orduser(models.Model):
	username = models.CharField(max_length=250)
	firstname = models.CharField(max_length=250)
	lastname = models.CharField(max_length=250)
	email = models.CharField(max_length=250)
	phone = models.CharField(max_length=100)
	address =  models.CharField(max_length=250)
	user_type = models.CharField(max_length=50,default="ordinaryuser")
	password1 = models.CharField(max_length=150)
	password2 = models.CharField(max_length=150)


	def __str__(self):
		return self.username

 
