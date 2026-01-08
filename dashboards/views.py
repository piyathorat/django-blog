from django.shortcuts import render,redirect,get_object_or_404
from blogs.models import Category,Blog
from .forms import CategoryForm,BlogPostForm
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
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

def posts(req):
    posts=Blog.objects.all()
    context={
        'posts':posts,
    }
    return render(req,'dashboard/posts.html',context)

def add_post(req):
    if req.method == "POST":
        form=BlogPostForm(req.POST,req.FILES)
        if form.is_valid():
            #take out the author name
            post=form.save(commit=False) #temporarilty saving the form
            post.author= req.user
            post.slug = slugify(post.title)
            post.save() # we need id thats why we first save it then it will generate the id
            #title= form.cleaned_data['title']  # if we want to get one data from the req.POST we use it
            post.slug = f"{slugify(post.title)}-{post.id}" # to add in slug field its new built in func and add the unique id
            post.save() 
            return redirect('posts')
        else:
            print('form is invalid')
            print(form.errors)
    form=BlogPostForm()
    context={
        'form':form,
    }
    return render(req,'dashboard/add_post.html',context)

def edit_post(req,pk):
    post=get_object_or_404(Blog,pk=pk)#to get all the data
    if req.method=="POST":
        form=BlogPostForm(req.POST,req.FILES,instance=post) #we need instance because we need curr data to show
        if form.is_valid():
            post=form.save()
            title=form.cleaned_data['title']
            post.slug=slugify(title)+'-'+str(post.id)
            post.save()
            return redirect('posts')
    form=BlogPostForm(instance=post)
    context={
        'form':form,
        'post':post,
    }
    return render(req,'dashboard/edit_post.html',context)


def delete_post(req,pk):
    post=get_object_or_404(Blog,pk=pk)
    post.delete()
    return redirect('posts')