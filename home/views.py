
from django.shortcuts import render
from article.models import Article, Category, Tag

def homepage(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'home/index.html', {'articles': articles, 'categories': categories, 'tags': tags})