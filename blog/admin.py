from django.contrib import admin
from . models import BlogPost
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title','sub_title','created_at']
    
    
admin.site.register(BlogPost,BlogPostAdmin)
