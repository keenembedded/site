
# Create your views here.

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

def index(request):
    return render(request,"index.html")

def product(request):
    return render(request,"product.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method == "POST":
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        contact = Contact(firstName=first_name,lastName = last_name,email = email,desc=desc)
        contact.save()
        messages.success(request, 'your detels are sent succesfully')
    return render(request, "contact.html")