
from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from django.db.models import F

def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    articles = Article.objects.all()
    Article.objects.filter(slug=slug).update(viewscounter=F('viewscounter') + 1)

    return render(request, 'article/article_details.html', {'article': article, 'articles': articles})


