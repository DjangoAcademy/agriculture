
from django.shortcuts import render
from article.models import Article, Category, Tag
from django.core.paginator import Paginator
from django.db.models import Q


def homepage(request):
    articles_list = Article.objects.all()
    query = request.GET.get('search')
    if query:
        articles_list = articles_list.filter(Q(title__icontains=query) |
                                             Q(category__name__icontains=query) |
                                             Q(tags__name__icontains=query) |
                                             Q(content__icontains=query)
                                             ).distinct()

    paginator = Paginator(articles_list, 2)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    mostviewed = Article.objects.all().order_by('-viewscounter')
    return render(request, 'home/index.html', {'articles': articles, 'mostviewed': mostviewed, 'categories': categories, 'tags': tags})