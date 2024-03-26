from django.shortcuts import render
from .models import BlogPost
# Create your views here.
def blog(request):
    blogs = BlogPost.objects.all()
    return render(request,'blog/blog.html',{'blogs':blogs})

def read_blog(request,post_id):
    blog = BlogPost.objects.get(id = post_id)
    return render(request,'blog/read_blog.html',{'blog':blog})
