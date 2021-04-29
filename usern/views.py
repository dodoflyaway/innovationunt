from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import orduser
#from innovator.models import sitetrans

# Create your views here.



def signupn(response):
	if response.method == "POST":
		if response.POST['username'] and  response.POST['firstname'] and response.POST['lastname'] and response.POST['email'] and response.POST['phone'] and response.POST['address'] and response.POST['password1'] and response.POST['password2']:
			
			print(response.POST)
			usersign = orduser()
			check = orduser.objects.values_list('username',flat=True)
			username_recived = response.POST['username'] 

			if username_recived in check:
				return render(response,'usern/signupn.html', {'error':'user already exist'})
			else:
				usersign.username = response.POST['username']

			usersign.firstname = response.POST['firstname']
			usersign.lastname = response.POST['lastname']
			usersign.email = response.POST['email']
			usersign.address = response.POST['address']
			usersign.phone = response.POST['phone']

			if response.POST['password1'] == response.POST['password2']:
				usersign.password1 = response.POST['password1']
				usersign.password2 = response.POST['password2']
			else:
				return render(response,'usern/signupn.html', {'error':'Both passwords must match'})
			
			usersign.save()
			return redirect('loginn')


		else:
			return render(response,'usern/signupn.html', {'error':'All field are required.'})

	else:
		return render(response,'usern/signupn.html')

	return render(response,'usern/signupn.html')


def loginn(response):
	nusersign = orduser()
	global ntokken
	ntokken = "npass"
	if response.method == "POST":
		try:
			nuserobj = orduser.objects.get(username=response.POST['username'])
		except Exception:
			return render(response,'usern/loginn.html', {'error':'User name or password in not valid.'})

		print(nuserobj)

		if response.POST['username'] == str(nuserobj):
			if str(nuserobj.password1) == str(response.POST['password1']):
				return redirect("/home/"+str(2)+str('/')+str(nuserobj))
			else:
				return render(response,'usern/loginn.html', {'error':'User name or Password in not valid.'})

	return render(response,'usern/loginn.html')


def ret():
    

	try:
		print(ntokken)
	except Exception:
		return redirect("/login",{'error':'you are not logged in '})

	return(ntokken)