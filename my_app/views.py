from django.shortcuts import render
from .models import ContactModel

# Create your views here.

def home(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        print(name, email, comment)
        obj = ContactModel(name=name, email=email, comment=comment)
        obj.save()
        
    return render(request, 'home.html')

def mypage(request):
    return render(request, 'cv.html')
    