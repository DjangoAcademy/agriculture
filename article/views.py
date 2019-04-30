
from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Tag
from django.db.models import F
from django.core.paginator import Paginator

def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    Article.objects.filter(slug=slug).update(viewscounter=F('viewscounter') + 1)
    mostviewed = Article.objects.all().order_by('-viewscounter')
    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'article/article_details.html', {'article': article, 'mostviewed': mostviewed, 'categories': categories, 'tags': tags})


def bycategory(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.all()
    articles_list = Article.objects.filter(category=category)
    paginator = Paginator(articles_list, 2)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    mostviewed = Article.objects.all().order_by('-viewscounter')
    tags = Tag.objects.all()

    return render(request, 'article/bycategory.html', {'category': category, 'categories': categories, 'articles': articles, 'mostviewed': mostviewed, 'tags': tags})


def bytag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    tags = Tag.objects.all()
    articles_list = Article.objects.filter(tags__in=[tag])
    paginator = Paginator(articles_list, 2)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    mostviewed = Article.objects.all().order_by('-viewscounter')
    categories = Category.objects.all()

    return render(request, 'article/bytag.html', {'tag': tag, 'tags': tags, 'categories': categories, 'articles': articles, 'mostviewed': mostviewed})






