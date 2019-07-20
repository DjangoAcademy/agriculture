
from django.shortcuts import render
from article.models import Category

def about(request):

    categories = Category.objects.all()

    return render(request, 'about/about.html', {'categories': categories})