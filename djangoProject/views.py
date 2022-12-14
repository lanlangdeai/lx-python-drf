#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from djangoProject.serializers import UserSerializer, GroupSerizlizer


class UserViewSet(viewsets.ModelViewSet):
    """
    查看与编辑用户api
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    查看与编辑api
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerizlizer











