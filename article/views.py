
from django.shortcuts import render, get_object_or_404
from .models import Article, Category

def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    articles = Article.objects.all()
    # category = Category.objects.all()

    return render(request, 'article/article_details.html', {'article': article, 'articles': articles})