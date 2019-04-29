
from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Tag
from django.db.models import F

def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    articles = Article.objects.all()
    Article.objects.filter(slug=slug).update(viewscounter=F('viewscounter') + 1)

    return render(request, 'article/article_details.html', {'article': article, 'articles': articles})


def bycategory(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category=category)

    return render(request, 'article/bycategory.html', {'articles': articles})


def bytag(request, slug):
    tag = get_object_or_404(Tag)
    articles = Article.objects.filter(tags=tag)

    return render(request, 'article')






