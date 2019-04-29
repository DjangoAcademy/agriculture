
from django.shortcuts import render
from article.models import Article, Category, Tag
from django.core.paginator import Paginator

def homepage(request):
    articles_list = Article.objects.all()
    paginator = Paginator(articles_list, 2)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    mostviewed = Article.objects.all().order_by('-viewscounter')
    return render(request, 'home/index.html', {'articles': articles, 'mostviewed': mostviewed, 'categories': categories, 'tags': tags})