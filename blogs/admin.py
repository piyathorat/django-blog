from django.contrib import admin
from . models import Category,Blog,Comment

# Register your models here.
admin.site.register(Category)


class BlogAdmin(admin.ModelAdmin):   #its for autognerated slug
    prepopulated_fields={'slug':('title',)}
    list_display=('title','category','author','status','is_featured')
    search_fields=('id','title','category__category_name','status')#its foreignkey field thats why
    list_editable=('is_featured',)

admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment)