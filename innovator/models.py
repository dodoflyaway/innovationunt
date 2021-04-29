from django.db import models
from usern.models import orduser
from django.contrib.auth.models import User

class invuser(models.Model):
	username = models.CharField(max_length=250)
	firstname = models.CharField(max_length=250)
	lastname = models.CharField(max_length=250)
	email = models.CharField(max_length=250)
	phone = models.CharField(max_length=100)
	address =  models.CharField(max_length=250)
	user_type = models.CharField(max_length=50,default="innovator")
	password1 = models.CharField(max_length=150)
	password2 = models.CharField(max_length=150)

	def __str__(self):
		return self.username


class product(models.Model):
	title = models.CharField(max_length=250)
	pub_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to='images/')
	icon = models.ImageField(upload_to='images/')
	prostatus = models.CharField(max_length=200)
	postedby = models.ForeignKey(invuser, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:100] + ' ...'

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')



'''
class subcribe(models.Model):
    link = models.ForeignKey(invuser, on_delete=models.CASCADE)
    sub_username = models.CharField(max_length=200)
    ordinary_username = models.CharField(max_length=200)

    def __str__(self):          you can never return the foreignkey 
    	return self.sub_username
'''


class sub(models.Model):
	sub_username = models.ForeignKey(invuser, on_delete=models.CASCADE)
	ordinary_username = models.CharField(max_length=200)
	mix = models.CharField(max_length=200)

	def __str__(self):
		return self.mix


class comment(models.Model):
	conid = models.ForeignKey(product,on_delete=models.CASCADE)
	inusername = models.CharField(max_length=200)
	ordusername = models.CharField(max_length=200)
	commentz = models.CharField(max_length=500)

	def __str__(self):
		return self.commentz


class sitetrans(models.Model):
	holder = models.ForeignKey(orduser,on_delete=models.CASCADE)
	donateusername = models.CharField(max_length=200)
	transdate = models.DateTimeField()
	amount = models.IntegerField()
	key = models.IntegerField()

	def __str__(self):
		return self.donateusername



class invtokenacc(models.Model):
	inuser = models.ForeignKey(invuser,on_delete=models.CASCADE)
	husername = models.CharField(max_length=200)
	donateusername = models.ForeignKey(sitetrans,on_delete=models.CASCADE)
	amount = models.IntegerField()
	mixd = models.CharField(max_length=350)
	keyh = models.ForeignKey(product,on_delete=models.CASCADE)

	def __str__(self):
		return self.mixd


class todo(models.Model):
	title = models.CharField(max_length=350)
	description = models.CharField(max_length=350)
	status = models.CharField(max_length=100)
	product = models.ForeignKey(product,on_delete=models.CASCADE)

	def __str__(self):
		return self.title






