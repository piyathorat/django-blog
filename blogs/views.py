from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Blog,Category
# Create your views here.
def posts_by_category(request, category_id):
    #fetch the post thats belongs to category with id and category_id
    posts=Blog.objects.filter(status="Published",category=category_id)
    # try: #whenever  we use get() try to do in try block because if 65 category doesnt exist then what?
        #  category=Category.objects.get(pk=category_id) # we want only one data thats why its get() 
    # except:
         #redirect user to home
        #  return redirect('404.html')
    category=get_object_or_404(Category,pk=category_id) #second method 404  show the error page
    context={
        'posts':posts,
        'category':category
    }
    
    return render(request,'post_by_category.html',context) 