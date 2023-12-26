from django.shortcuts import render,redirect
from .models import User,Contact
from django.conf import settings
from django.core.mail import send_mail
import random
from django.http import JsonResponse

def validate_signup(request):
	email=request.GET.get('email')
	print(email)
	data={
		'is_taken':User.objects.filter(email__iexact=email).exists()
	}
	return JsonResponse(data)

def index(request):
	return render(request,'index.html')

def about(request):
	if request.method=="POST":
		Contact.objects.create(
					name=request.POST['name'],
					mobile=request.POST['mobile'],
					email=request.POST['email'],
					message=request.POST['message']
				)
		msg="Your Information Is Sent Successfully"
		return render(request,'about.html',{'msg':msg})
	else:
		return render(request,'about.html')

def departments(request):
	return render(request,'departments.html')

def doctors(request):
	return render(request,'doctors.html')

def doc1(request):
	return render(request,'doc1.html')

def doc2(request):
	return render(request,'doc2.html')

def doc3(request):
	return render(request,'doc3.html')

def contact(request):
		return render(request,'contact.html')

def signup(request):
	if request.method=="POST":
		try:
			User.objects.get(email=request.POST['email'])
			msg="Email Already Registered"
			return render(request,'signup.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
					fname=request.POST['fname'],
					lname=request.POST['lname'],
					mobile=request.POST['mobile'],
					email=request.POST['email'],
					address=request.POST['address'],
					password=request.POST['password'],
					profile_pic=request.FILES['profile_pic']
				)
				msg="User Signed Up Successfully"
				return render(request,'login.html',{'msg':msg})
			else:
				msg="Password And Confirm Password does not match"
				return render(request,'signup.html',{'msg':msg})	
	else:
		return render(request,'signup.html')

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password==request.POST['password']:
				request.session['email']=user.email
				request.session['fname']=user.fname
				request.session['profile_pic']=user.profile_pic.url
				return render(request,'index.html')
			else:
				msg="Password Is Incorrect"
				return render(request,'login.html',{'msg':msg})
		except:
			msg="Email Not Registered"
			return render(request,'login.html',{'msg':msg})
	else:
		return render(request,'login.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		del request.session['profile_pic']
		return render(request,'login.html')
	except:
		return render(request,'login.html')


def forgot_password(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			otp=random.randint(1000,9999)
			subject = 'OTP For Frogot Password'
			message = 'Hello '+user.fname+',Your OTP For Frogot Password Is '+str(otp)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email, ]
			send_mail( subject, message, email_from, recipient_list )
			return render(request,'otp.html',{'email':user.email,'otp':otp})
		except:
			msg="Email Id Not Found"
			return render(request,'forgot_password.html',{'msg':msg})
	else:
		return render(request,'forgot_password.html')

def verify_otp(request):
	email=request.POST['email']
	otp=request.POST['otp']
	uotp=request.POST['uotp']
	if otp==uotp:
		return render(request,'new_password.html',{'email':email})
	else:
		msg="Invalid OTP"
		return render(request,'otp.html',{'email':email,'otp':otp,'msg':msg})

def new_password(request):
	email=request.POST['email']
	np=request.POST['new_password']
	cnp=request.POST['cnew_password']

	if np==cnp:
		user=User.objects.get(email=email)
		if user.password==np:
			msg="You cannot use this password"
			return render(request,'new_password.html',{'email':email,'msg':msg})
		else:	
			user.password=np
			user.save()
			msg="Password Updated Successfully"
			return render(request,'login.html',{'msg':msg})
	else:
		msg="New Password & Confirm New Password Does Not Match"
		return render(request,'new_password.html',{'email':email,'msg':msg})

def change_password(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])
		if user.password==request.POST['old_password']:
			if request.POST['new_password']==request.POST['cnew_password']:
				user.password=request.POST['new_password']
				user.save()
				return redirect('logout')
			else:
				msg="New Password & Confirm New Password Does Not Match"
				return render(request,'change_password.html',{'msg':msg})
		else:
			msg="Old Password Does Not Match"
			return render(request,'change_password.html',{'msg':msg})
	else:
		return render(request,'change_password.html')

def profile(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		user.fname=request.POST['fname']
		user.lname=request.POST['lname']
		user.mobile=request.POST['mobile']
		user.address=request.POST['address']
		try:
			user.profile_pic=request.FILES['profile_pic']
		except:
			pass
		user.save()
		request.session['profile_pic']=user.profile_pic.url
		msg="Profile Updated Successfully"
		return render(request,'profile.html',{'user':user,'msg':msg})
	else:
		return render(request,'profile.html',{'user':user})

def pcos(request):
	return render(request,'pcos.html')

def pcod(request):
	return render(request,'pcod.html')

def menopause(request):
	return render(request,'menopause.html')

def menstrual_hygiene(request):
	return render(request,'menstrual_hygiene.html')


def faq(request):
	return render(request,'faq.html')

def product(request):
	return render(request,'product.html')


