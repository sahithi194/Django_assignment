from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def HomePage(request):
    return render(request,'Template_path\homepage.html')

def IndexPage(request):
    return render(request,'Template_path\indexpage.html')