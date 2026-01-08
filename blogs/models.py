from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=50,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:  #its for plural categorys to ==
        verbose_name_plural='categories'

    def __str__(self): #its used for admin panel not to return object1 return name
        return self.category_name
    
STATUS_CHOICES=(
    ("Draft",'Draft'),
    ("Published","Published")
)
class Blog(models.Model):

    title = models.CharField(max_length=100)
    # Stores the blog title (e.g., "Introduction to Django")

    slug = models.SlugField(max_length=150, unique=True, blank=True)
    # URL-friendly version of the title (used in URLs)
    # Example: "introduction-to-django"
    # unique=True → no two blogs can have same slug
    # blank=True → slug can be auto-generated

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Links blog to a category (one category → many blogs) 
    # CASCADE → delete blogs if category is deleted

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Links blog to a user (author)
    # CASCADE → delete blogs if author is deleted

    featured_img = models.ImageField(upload_to='uploads/%Y/%m/%d')
    # Stores blog image
    # Uploaded to: uploads/year/month/day/

    short_description = models.TextField(max_length=500)
    # Short summary of blog (used in cards & previews)

    blog_body = models.TextField(max_length=2000)
    # Full blog content/article

    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default="Draft")
    # Blog status (Draft / Published)
    # Choices defined in STATUS_CHOICES

    is_featured = models.BooleanField(default=False)
    # Marks blog as featured (shown on homepage)

    created_at = models.DateTimeField(auto_now_add=True)
    # Stores date & time when blog is created

    updated_at = models.DateTimeField(auto_now=True)
    # Updates date & time whenever blog is edited

    def __str__(self): #its used for admin panel not to return object1 return name
        return self.title

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)#blog is deleted then comments also will deleted
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment=models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    # Stores date & time when blog is created

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
