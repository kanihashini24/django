from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .models import Datas

from django.template import loader
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())


def navigation(request):
    template = loader.get_template('navbar.html')
    return HttpResponse(template.render())

def home1(request):
    return HttpResponse("Hello, Django!")
def hai(request):
    return HttpResponse("welcome to my django project!")




def home(request):  # 127.0.0.1:8000/
    mydata=Datas.objects.all()
    if(mydata!=""):
        return render(request,"contact.html",{"datas":mydata})
    else:
        return render(request,"contact.html")    
      
    

def addData(request):
    if request.method=="POST":
        name=request.POST["firstname"]
        age=request.POST["age"]
      
        address=request.POST["address"]
        mail=request.POST["mail"]
        
        obj=Datas()
        obj.Name=name
        obj.Age=age
     
        obj.Address=address
        obj.Mail=mail
        obj.save()
        mydata=Datas.objects.all()
        return redirect("about")
    return render(request,"contact.html")

def updateData(request,id):
    mydata=Datas.objects.get(id=id)
    if request.method=="POST":
        name=request.POST["name"]
        age=request.POST["age"]

        address=request.POST["address"]
        mail=request.POST["mail"]
        
        mydata.Name=name
        mydata.Age=age

        mydata.Address=address
        mydata.Mail=mail
        mydata.save()
        return redirect("home")
    return render(request,"update.html",{"data":mydata})

def deleteData(request,id):
    mydata=Datas.objects.get(id=id)
    mydata.delete()
    return redirect("home")
