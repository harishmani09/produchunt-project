from django.shortcuts import render
from .models import Products
# Create your views here.
def home(request):
    return render(request,'products/home.html')