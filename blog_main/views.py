
from django.http import HttpResponse
from django.shortcuts import render,redirect
from blogs.models import Category,Blog
from assignments.models import About
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
def home(request):
    featured_post=Blog.objects.filter(is_featured=True,status='Published').order_by('-updated_at') #filter because we have to add cond
    posts=Blog.objects.filter(is_featured=False, status='Published')
    #fetch about us
    try:#try only works with get() not with all() and filter()
        about=About.objects.get()
    except:
        about=None
    context={
        'featured_post':featured_post,
        'posts':posts,
        'about':about
    }
    return render(request ,"home.html",context) #context will only take one function for the categories we have dine the context processor 

def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form=RegistrationForm()
    context={
        'form':form,
    }
    return render(request,"register.html",context)


def login(request):
    if request.method=="POST":
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']#cleaned_data gives you safe, validated, and cleaned input from the form.
            password=form.cleaned_data['password']

            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
            return redirect('home')
    form=AuthenticationForm()   # we dont need any extra field thats why authentication and when we need to create then it will userrregistration()
    context={
        'form':form,
    }
    return render(request,'login.html',context)

def logout(request):
    auth.logout(request)
    return redirect('home')