from django import forms
from blogs.models import Category,Blog
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__' #to get all fields


class BlogPostForm(forms.ModelForm):
    class Meta:
        model=Blog
        #fields='__all__'  # we dont need all the fields  author and slug it should be assign by programmitically
        fields=('title','category','featured_img','short_description','blog_body','status','is_featured')

