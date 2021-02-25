from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import a

# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    # return HttpResponse("this is a home page")
    return render(request,'home.html')
def about(request):
    # return HttpResponse("this is a about page")
    return render(request, 'about.html')
def contact(request):
    # return HttpResponse("this is a contact page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = a(name =name,email =email, phone =phone , desc=desc)#date =datetime.today()) #CREATING OBJECT OF Contact
        contact.save()
    return render(request, 'contact.html')

def services(request):
    # return HttpResponse("this is a services page")
    return render(request, 'services.html')