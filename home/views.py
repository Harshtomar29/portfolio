from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import Service
from django.contrib import messages


# Create your views here.
def index (request):

     context= {
         "variable1" : "Harsh is great",
         "variable2" : "Harry is great"

     }

     return render (request , 'index.html', context)   
   # return HttpResponse("this is homepage")

def about (request):

    return render (request,'about.html')
   # return HttpResponse("this is aboutpage")

def services (request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        services = Service(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        services.save()
        
        messages.success(request, 'Your message has been sent!')


    return render (request,'services.html')
    #r eturn HttpResponse("this is services page")
#make migration and migrate ka khyal rakhna h

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        
        messages.success(request, 'Your message has been sent!')

    return render(request, 'contact.html')


 
     
      


#https://source.unsplash.com/daily"


#https://source.unsplash.com/1600x600/?icecream,ice