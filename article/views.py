from django.shortcuts import render
from .models import Article
from rest_framework import viewsets
from .serizlizers import ArticleSerializer, ArticleHaystackSerializer
from drf_haystack.viewsets import HaystackViewSet
from utils.custom_exception import CustomException
from rest_framework.throttling import UserRateThrottle

import logging

logger = logging.getLogger("demo")


class ArticleSearchView(HaystackViewSet):
    index_models = [Article]
    serializer_class = ArticleHaystackSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()

    throttle_classes = (UserRateThrottle,)
    serializer_class = ArticleSerializer
    logger.error("error msg")

    # @action(detail=False, methods=['get'], url_name='exception', url_path='exception')
    # def exception(self, request, *args, **kwargs):
    #     logger.error('自定义异常')
    #     raise CustomException(data={'detail': '自定义异常'})


# 基于view的限流
# @throttle_classes([UserRateThrottle])
