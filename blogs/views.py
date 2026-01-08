from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from .models import Blog,Category,Comment
from django.db.models import Q
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

def blogs(request,slug):
    single_blog=get_object_or_404(Blog,slug=slug, status='Published')
    if request.method == "POST":
        comment=Comment()
        comment.user=request.user
        comment.blog=single_blog
        comment.comment=request.POST['comment']             #inside the name attribute
        comment.save()
        return HttpResponseRedirect(request.path_info) # it will take u where u came from

    #comments
    comments=Comment.objects.filter(blog=single_blog)
    comment_count=comments.count()
    context= {
        'single_blog':single_blog ,
        'comments':comments,
        'comment_count':comment_count,
    }
    return render(request,'blogs.html',context)

def search(request):
    keyword=request.GET.get('keyword')
    blogs=Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword)| Q(blog_body__icontains=keyword) , status='Published' ) # , is and oprator | it means or operator so to use operator we have to iimport Q means Querry set  and there i means any uppercase and lowercase is allow
    context={
        'blogs':blogs,
        'keyword':keyword,
        
    }
    return render(request,'search.html' , context)