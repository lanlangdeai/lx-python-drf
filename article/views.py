from django.shortcuts import render
from .models import Article
from rest_framework import viewsets
from .serizlizers import ArticleSerializer, ArticleHaystackSerializer
from drf_haystack.viewsets import HaystackViewSet


class ArticleSearchView(HaystackViewSet):
    index_models = [Article]
    serializer_class = ArticleHaystackSerializer



class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer









