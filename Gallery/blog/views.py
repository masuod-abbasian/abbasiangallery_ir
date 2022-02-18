from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.shortcuts import render , get_object_or_404
from .models import Article, Category
from django.contrib.auth.models import User
# Create your views here.

'''
# home page with func view
def Blog_Home(request, page=1):
    article_list = Article.objects.article_publish()
    paginator = Paginator(article_list, 3)
    articles = paginator.get_page(page)
    context = {
        "articles" : articles
    }
    return render(request, 'blog/blog-home.html', context)
'''
# home page with generic view
class ArticleList(ListView):
    queryset = Article.objects.article_publish()
    paginate_by = 3

'''
# detail with func view
def Detail(request, slug):
    a = Article.objects.filter(status='p')
    context = {
        "article": get_object_or_404(Article.objects.article_publish(), slug=slug),
    }
    return render(request, 'blog/detail.html', context)
'''
# detail with generic view
class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.article_publish(), slug=slug)

'''
def category(request ,slug ,page=1):
    category = get_object_or_404(Category, slug=slug, status=True)
    category_list = category.articles.article_publish()
    paginator = Paginator(category_list, 3)
    articles = paginator.get_page(page)
    context = {
        'category': category,
        'articles': articles
    }
    return render(request, 'blog/category.html', context)
'''


# category with generic view
class CategoryList(ListView):
    paginate_by = 3
    template_name = 'blog/category_list.html'
    
    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.article_publish()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context

# author with generic view
class AuthorList(ListView):
    paginate_by = 3
    template_name = 'blog/author_list.html'
    
    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.articles.article_publish()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context