from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request,'app\index.html')
def ecom(request):
    return render(request,'app\ecom.html')
