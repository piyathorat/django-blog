
from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category,Blog
def home(request):
    featured_post=Blog.objects.filter(is_featured=True,status='Published').order_by('-updated_at') #filter because we have to add cond
    posts=Blog.objects.filter(is_featured=False, status='Published')
    context={
        'featured_post':featured_post,
        'posts':posts,
    }
    return render(request ,"home.html",context) #context will only take one function for the categories we have dine the context processor 