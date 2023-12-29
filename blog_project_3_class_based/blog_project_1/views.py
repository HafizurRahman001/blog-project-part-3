from django.shortcuts import render
from posts_app.models import Post
from categories_app.models import Category

# Create your views here.
def home(request, category_slug = None):
    post_data = Post.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug=category_slug)
        post_data = Post.objects.filter(category = category)
    category_data = Category.objects.all()
    return render(request,'displayData.html', {'postData':post_data, 'categories':category_data})