from django.shortcuts import render , get_object_or_404
from .models import Article
# Create your views here.
def Blog_Home(request):
    context = {
        "articles" : Article.objects.filter(status='p')
    }
    return render(request, 'blog/blog-home.html', context)

def Detail(request, slug):
    context = {
        "article": get_object_or_404(Article, slug=slug, status='p')
    }
    return render(request, 'blog/detail.html', context)