#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication

from django.conf.urls import url

class AnyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        return

@api_view(['POST'])
@authentication_classes((AnyAuthentication,))
@permission_classes((AllowAny,))
def login(request):
    token = request.COOKIES.get('auth', 'auth')
    password = request.data.get('password', '')
    username = request.data.get('username', '')

    response = Response({'user': 'user_info', 'token': token})
    response.set_cookie('auth', token, domain='0.0.0.0', expires=30 * 24 * 60 * 60)
    return response


@api_view(['GET'])
@authentication_classes((AnyAuthentication))

def check_token(request, token):
    token = request.COOKIES.get('auth')

    data = {
        "user_info": {
            "username": "admin",
            "user_id": 1
        },
        "token": token
    }
    return Response(data)










