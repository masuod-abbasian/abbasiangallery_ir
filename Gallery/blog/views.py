from django.core.paginator import Paginator
from django.shortcuts import render , get_object_or_404
from .models import Article, Category
# Create your views here.

def Blog_Home(request, page=1):
    article_list = Article.objects.article_publish()
    paginator = Paginator(article_list, 3)
    articles = paginator.get_page(page)
    context = {
        "articles" : articles
    }
    return render(request, 'blog/blog-home.html', context)

def Detail(request, slug):
    a = Article.objects.filter(status='p')
    context = {
        "article": get_object_or_404(Article.objects.article_publish(), slug=slug),
    }
    return render(request, 'blog/detail.html', context)

def category(request ,slug):
    context = {
        'category': get_object_or_404(Category, slug=slug, status=True)
    }
    return render(request, 'blog/category.html', context)