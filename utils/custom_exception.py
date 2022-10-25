#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


class CustomException(Exception):

    default_code = 400
    default_message = None

    def __init__(
        self,
        status_code=status.HTTP_400_BAD_REQUEST,
        code: int = None,
        message: str = None,
        data=None,
    ):
        self.code = code
        self.status = (status_code,)
        self.message = message

        if data is None:
            self.data = {"detail": self.message, "code": self.code}
        else:
            self.data = data

    def __str__(self):
        return str(self.code) + self.message


class ExecuteError(CustomException):
    default_code = 500
    default_message = "执行错误"


class UnknownError(CustomException):
    default_code = 500
    default_message = "位置错误"


def custom_exception_handler(exc, context):
    if isinstance(exc, CustomException):
        return Response(data=exc.data, status=exc.status)
    response = exception_handler(exc, context)
    return response
