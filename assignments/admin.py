from django.contrib import admin
from .models import About,SocialLink
# Register your models here.


class AboutAdmin(admin.ModelAdmin):  # we can add only about  so we are hiding the button with overrride then the btn will hide its built in method
    def has_add_permission(self, request):
        count=About.objects.all().count()
        if count==0:
            return True
        return False
admin.site.register(About , AboutAdmin)
admin.site.register(SocialLink)