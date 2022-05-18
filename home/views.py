from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    #return HttpResponse("This is my homepage (/homepage)")
    context = {'name': 'Kamal', 'course': 'Django'}
    return render(request,'home.html',context)

def contact(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        #print(name,email,phone,desc)
        ins = Contact(name =name, email = email, phone = phone, desc = desc)
        ins.save()
        print("The data has been returned to the db")
        
        
    
    #return HttpResponse("This is my contact page (/contact)")
    return render(request, 'contact.html')

def About(request):
    #return HttpResponse("This is my About page (/About)")
    return render(request,'About.html')

def projects(request):
    #return HttpResponse("This is my projects page (/projects)")
    return render(request,'projects.html')