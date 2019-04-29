
from django.urls import path
from article import views

urlpatterns = [
    path('articles/<str:slug>/', views.article_details, name='article_details'),
    path('categories/<str:slug>/', views.bycategory, name='bycategory'),
]