from django.shortcuts import render
from django.http import HttpResponse



# djangousername-djangoadmin
# djangopassword-dheeraj@123




def home(request):
    return render(request, 'home.html')