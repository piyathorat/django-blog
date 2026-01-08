from django.shortcuts import render,redirect,get_object_or_404
from blogs.models import Category,Blog
from .forms import CategoryForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def dashboard(req):
    category_count=Category.objects.all().count()
    blogs_count=Blog.objects.all().count()
    context={
        "category_count":category_count,
        "blogs_count":blogs_count,

    }
    return render(req,"dashboard/dashboard.html" , context)


def categories(req):
    return render(req,"dashboard/categories.html")

def add_category(req):
    if req.method=='POST':
        form=CategoryForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form=CategoryForm()
    context={
        'form':form
    }
    return render(req,"dashboard/add_category.html",context)

def edit_category(req,pk):
    category=get_object_or_404(Category,pk=pk)
    if req.method=="POST":
        form =CategoryForm(req.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form= CategoryForm(instance=category)
    context={
        'form':form,
        'category':category,
    }
    return render(req,'dashboard/edit_category.html',context)


def delete_category(req,pk):
    category=get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')