from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from ApiApp.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate
from django.utils import timezone

@csrf_exempt
def reg(request):
	return render(request,'reg.html')	

@csrf_exempt
def savereg(request):
		a=username=request.POST.get("ausername")
		b=firstname=request.POST.get("afirstname")
		c=lastname=request.POST.get("alastname")
		d=email=request.POST.get("aemailid")
		e=password=request.POST.get("apassword")

		obj=User(username=a,firstname=b,lastname=c,emailid=d,password=e)
		obj.save()
		msg="User Created"
		return HttpResponse(msg)	
		
@csrf_exempt
def login(request):
	return  render(request,'login.html')

@csrf_exempt
def mlogin(request):
	a=request.POST.get('ausername')
	b=request.POST.get('apassword')

	obj = User.objects.filter(username=a,password=b)
	if obj:
		return render(request,'welcome.html')
	else:
		return render(request,'fail.html')	

def welcome(request):
	return render(request,'welcome.html')		

def fail(request):
	return render(request,'fail.html')		

