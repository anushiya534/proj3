from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	return render(request,'index.html')
def login(request):
	return render(request,'login.html')
def registration(request):
    return render(request,'registration.html')
def home(request):
 	return render(request,'home.html')
def Artist(request):
	return render(request,'Artist.html')
def contact(request):
	return render(request,'contact.html')
def submit(request):
	return render(request,'submit.html')
def buy(request):
	return render(request,'buy.html')
def order(request):
	return render(request,'order.html')
def buy1(request):
	return render(request,'buy1.html')
def buy2(request):
	return render(request,'buy2.html')

def order1(request):
	return render(request,'order1.html')
def order2(request):
	return render(request,'order2.html')




    