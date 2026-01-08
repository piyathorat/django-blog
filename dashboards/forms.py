from django import forms
from blogs.models import Category,Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__' #to get all fields


class BlogPostForm(forms.ModelForm):
    class Meta:
        model=Blog
        #fields='__all__'  # we dont need all the fields  author and slug it should be assign by programmitically
        fields=('title','category','featured_img','short_description','blog_body','status','is_featured')

class AddUserForm(UserCreationForm): #it take care of new users
    class Meta:
        model=User
        fields=('username','email','first_name','last_name','email','is_active','is_staff','is_superuser','groups','user_permissions')
        

class EditUserForm(forms.ModelForm):
    class Meta:
        model =User
        fields=('username','email','first_name','last_name','email','is_active','is_staff','is_superuser','groups','user_permissions')
