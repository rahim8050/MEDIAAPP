from django.shortcuts import render
# Create your views here.
def home(request):
    return  render(request,'homepage.html')


def signup(request):
    return render(request,'signup.html')


def profile(request):
    return render(request,'profile.html')


def signin(request):
    return render(request,'signin.html')