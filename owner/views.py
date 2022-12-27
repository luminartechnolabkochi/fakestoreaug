from django.shortcuts import render

# Create your views here
from django.views.generic import View
from owner.forms import  LoginForm,RegistrationForm

class HomeView(View):

    def get(self,request,*args,**kwargs):


        return render(request,"home.html")

class SignUpView(View):

    def get(self,request,*args,**kwargs):
        form=RegistrationForm()

        return render(request,"register.html",{"form":form})

class SignInView(View):
    def get(self,request,*args,**kw):
        form=LoginForm()
        return render(request,"login.html",{"form":form})

    def post(self,request,*args,**kw):
        print(request.POST.get("username"))
        print(request.POST.get("password"))
        return render(request,"home.html")