from django.urls import path
from . import views
urlpatterns = [
    path('', views.blog, name = 'blog'),
    path('read_blog/<int:post_id>/', views.read_blog, name = 'read_blog'),
]