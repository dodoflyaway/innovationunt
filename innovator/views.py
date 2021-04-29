from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import invuser
from .models import product
from .models import sub
from .models import comment 
from .models import sitetrans
from .models import invtokenacc
from .models import todo
from usern.models import orduser
from django.utils import timezone
from usern import views as vk
# Create your views here.



def signup(response):
	if response.method == "POST":
		if response.POST['username'] and response.POST['firstname'] and response.POST['lastname'] and response.POST['email'] and response.POST['phone'] and response.POST['address'] and response.POST['password1'] and response.POST['password2']:   
			usersign = invuser()
			chk = invuser.objects.values_list('username',flat="True")  #ls = invuser.objects.values_list('firstname',flat="True")
			username_recived = response.POST['username'] #return render(response,'innovator/signup.html', {'error':'user already exist'})

			if username_recived in chk:
				return render(response,'innovator/signup.html', {'error':'user already exist'})
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
				return render(response,'innovator/signup.html', {'error':'Both passwords must match'})
			usersign.save()

		else:
			return render(response,'innovator/signup.html', {'error':'All field are required.'})
	else:
		return render(response,'innovator/signup.html')

   
	return render(response, 'innovator/signup.html')# {'user_info':user_info}


def login(response):
	#------------- USEFULL QUERY MANIPULATE DATA ----------
	# User.objects.get(username=request.POST['username'])
	# code to retrive a specfic element 
	# ch = invuser.objects.get(username="monis")
	# the related fields are now accessable 
	# ch.password1 
    # password = response.POST['password1']
    #from sample.models import Todolist,Item,user
	#ls = Todolist.objects.all()
	#ls = Todolist.objects.get(id=2)
	#user.objects.create(tasks=ls,user_name="monis")
	usersign = invuser()
	global tokken
	tokken = "pass"
	if response.method == "POST":
		try:
			userobj = invuser.objects.get(username=response.POST['username'])
		except Exception:
			return render(response,'innovator/login.html', {'error':'User name or password in not valid.'})


		if response.POST['username'] == str(userobj):
			if str(userobj.password1) == str(response.POST['password1']):
				global user
				user = userobj
				return redirect("/home/"+str(1)+str('/')+str(userobj))
			else:
				return render(response,'innovator/login.html', {'error':'User name or Password in not valid.'})

	return render(response, 'innovator/login.html')

global tok

def home(response,tok,user):

	if tok == 1:
		user_obj = invuser.objects.get(username=user)
	if tok == 2:
		user_obj = orduser.objects.get(username=user)
	
	global tokk 
	tokk = tok
	
	
	prod = product.objects.all()
	return render(response, 'innovator/home.html',{'user':user_obj,'product':prod,'tok':tok})



def create(response):
	try:
		print(tokken)
	except Exception:
		return redirect("/login",{'error':'you are not logged in '})

	

	if response.method == "POST":
		if response.POST['title'] and response.POST['body'] and response.POST['prostatus'] and response.FILES['icon'] and response.FILES['image']:
			prod = product()
			prod.title = response.POST['title']
			prod.body = response.POST['body']
			prod.icon = response.FILES['icon']
			prod.image = response.FILES['image']
			prod.prostatus = response.POST['prostatus']
			prod.pub_date = timezone.datetime.now()
			prod.postedby = user
			prod.save()
		return  redirect("/home/"+str(1)+str('/')+str(user))



	return render(response,'innovator/create.html')



def detail(response,product_id,username):
	if tokk == 1:
		pname = invuser.objects.get(username=username)
	elif tokk == 2:
		pname = orduser.objects.get(username=username)

	print(pname)

	prod = get_object_or_404(product,pk=product_id)
	return render(response,'innovator/detail.html',{'product':prod,'pname':pname})


def subcriber(response,product_id,username,creator):

	uqmix = str(username) + str(creator) # used to ensure that there in no other similar name and same person does not subcribe twice
	subb = sub()
	mix_r_list = sub.objects.values_list('mix',flat="True")
	print(mix_r_list)

	if uqmix in mix_r_list:
		print("in condtion")
		return render(response,'innovator/error.html',{'error':'you have already subcribed ','product_id':product_id,'username':username})
	else:
		print(creator+" creator")
		print(username+" username")
		pcreator = invuser.objects.get(username=creator)
		subb.sub_username = pcreator
		subb.ordinary_username = username
		subb.mix = uqmix
		subb.save()
	return redirect("/detail/"+str(product_id)+str("/")+str(username))


'''
___________________ ACCESSING USING FOREIGN KEY________________________
from innovator.models import invuser
ls = invuser.objects.get(username="random_travel_boiii_o") / you have to know the exact name 
ks = ls.sub_set.all()
for i in ks:
	print(i)
	print(i.orinary_username)
 This took me about 30 mins to figure out and iam loosing my mind 

'''

def showsubs(response,product_id,creator):
	userobj = invuser.objects.get(username=creator)
	return render(response,'innovator/showsub.html',{'userobj':userobj})


def commentmake(response,product_id,username):
	com = comment()
	prod = product.objects.get(id=product_id)
	x = prod.postedby.username
	print(prod.id)
	if response.method == 'POST':
		if response.POST['commentz']:
			com.conid = prod
			com.inusername = prod.postedby.username
			com.ordusername = username
			com.commentz = response.POST['commentz']
			com.save()
		else:
			return render(response,'innovator/commentmake.html', {'prod':prod,'username':username,'error':'All field are required'})
        
	else:
		return render(response,'innovator/commentmake.html',{'prod':prod,'username':username})


	return render(response,'innovator/commentmake.html',{'prod':prod,'username':username})


def commentshow(response,product_id,creator):
	print(creator)
	print(product_id)
	prod = product.objects.get(id=product_id)


	return render(response,'innovator/commentshow.html',{'prod':prod})



def buytoken(response,tok,username):
	user_obj = orduser.objects.get(username=username)
	tran = sitetrans()

	
	if response.method == 'POST':
		if response.POST['amount'] and response.POST['card_number'] and response.POST['expirydate'] and response.POST['CVV'] and response.POST['key']:
			int_amount = int(response.POST['amount']) #number input restriction
			int_card_number = int(response.POST['card_number'])
			int_key = int(response.POST['key'])
			int_CVV = int(response.POST['CVV'])
			flag_len_CVV = len(response.POST['CVV'])
			flag_len_key = len(response.POST['key'])
			flag_len_card_number = len(response.POST['card_number'])

			if flag_len_CVV != 3:
				return render(response,'innovator/buytoken.html',{'user_obj':user_obj,'tok':tok,'error':'Error CVV should  3 Digits '})

			if flag_len_key > 10:
				return render(response,'innovator/buytoken.html',{'user_obj':user_obj,'tok':tok,'error':'Key should not be greate than 10 digits '})

			if flag_len_key < 10:
				return render(response,'innovator/buytoken.html',{'user_obj':user_obj,'tok':tok,'error':'Key should not be less than  10 digits '})

			if flag_len_card_number != 16:
				return render(response,'innovator/buytoken.html',{'user_obj':user_obj,'tok':tok,'error':' Card number should be 16 digits  '})

			holder_r_list = sitetrans.objects.values_list('donateusername',flat="True") 
			print(holder_r_list)
			if username in holder_r_list:                                   
				update_obj = sitetrans.objects.get(donateusername=username)
				update_obj.amount = update_obj.amount + int_amount
				update_obj.save()
				return  redirect("/home/"+str(tok)+str('/')+str(username))
			else:        
				tran.holder = user_obj
				tran.donateusername = username
				tran.transdate = timezone.datetime.now()
				tran.amount = int_amount
				tran.key = int_key
				tran.save()
				return  redirect("/home/"+str(tok)+str('/')+str(username))



		else:
			return render(response,'innovator/buytoken.html',{'user_obj':user_obj,'tok':tok,'error':'All field are required'})
	else:
		return render(response,'innovator/buytoken.html',{'user_obj':user_obj,'tok':tok})

	return render(response,'innovator/buytoken.html',{'user_obj':user_obj,'tok':tok})


def tokendonate(response,product_id,username,creator):
	acc = invtokenacc()
	mixk = str(username) + str(creator)
	donation_list = invtokenacc.objects.values_list('mixd',flat=True) #geting the list of existing user/inv pairs
	creator_obj = invuser.objects.get(username=creator) # inv user instance for foreign key
	product_obj = product.objects.get(id=product_id)
	tran_obj = sitetrans.objects.get(donateusername=username)
   

	if response.method == 'POST':
		if response.POST['amount'] and response.POST['key']:
			
			int_keyr_len = len(response.POST['key'])
			int_amount = int(response.POST['amount'])

			if int_keyr_len != 10:
				return render(response,'innovator/tokendonate.html',{'product_id':product_id,'username':username,'creator':creator,'error':'key should be 10 digits'})

			if mixk in donation_list:
				update_amount = invtokenacc.objects.get(mixd=mixk)
				tran_obj.amount = tran_obj.amount - int_amount
				update_amount.amount = update_amount.amount + int_amount    #checking if the person has donated already
				update_amount.save()
				tran_obj.save()
				return redirect("/detail/"+str(product_id)+str("/")+str(username))
			else:
				acc.inuser = creator_obj
				acc.husername = creator
				acc.donateusername = tran_obj
				tran_obj.amount = tran_obj.amount - int_amount
				acc.amount = int_amount
				acc.mixd = mixk
				acc.keyh = product_obj
				acc.save()
				tran_obj.save()
				return redirect("/detail/"+str(product_id)+str("/")+str(username))


		else:
			return render(response,'innovator/tokendonate.html',{'product_id':product_id,'username':username,'creator':creator,'error':'All field are required'})

	else:
		return render(response,'innovator/tokendonate.html',{'product_id':product_id,'username':username,'creator':creator})

	return render(response,'innovator/tokendonate.html',{'product_id':product_id,'username':username,'creator':creator})


def todoadd(response,product_id,creator):
	product_obj = product.objects.get(id=product_id)
	print(type(product_obj.prostatus))

	if product_obj.prostatus == "complete" or product_obj.prostatus == "completed" or product_obj.prostatus == "Completed" or product_obj.prostatus == "Complete":
		return render(response,'innovator/todoadd.html'{'error':'the project is completed no more activity can be added '})
	else:



	return render(response,'innovator/todoadd.html',{'product_id':product_id,'creator':creator})
