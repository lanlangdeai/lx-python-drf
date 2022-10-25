#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from django.utils.translation import ugettext_lazy
from django.contrib.auth.models import User

class MyAuthentication(BaseAuthentication):

    def authenticate(self, request):
        token = request.COOKIES.get('auth')

        if token is not None:
            username = self.check_token(token)
            if username is not None:
                return User.objects.get(username=username), token
            else:
                raise exceptions.AuthenticationFailed(ugettext_lazy('invalid token'))

    @staticmethod
    def check_token(token):
        response = requests.get('http://localhost:8000/check_token/' + token)
        if response.status_code == 200:
            return response.json().get('user_info', {}).get('username')




