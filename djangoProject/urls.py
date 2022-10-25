"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from rest_framework import routers, permissions
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from . import views
from .mock_view import login, check_token
from article.urls import urlpatterns as article_urls


schema_view = get_schema_view(
    openapi.Info(
        title="drf ai",
        default_version="v1",
        description="drf desc",
        terms_of_service="",
        contact=openapi.Contact(email="admin@admin.com"),
        license=openapi.License(name="bsd license"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)

urlpatterns = [
    url(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    url(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    url(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    url(r"^", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api-auth", include("rest_framework.urls")),
    url(r"^jwt-token-verify/", verify_jwt_token),
    url(r"^jwt-token-auth/", obtain_jwt_token),
    path("api/", include(article_urls)),
]


mock_urls = [
    url("^login/", login),
    url("^check_token/(?P<token>[A-Za-z0-9]/$)", check_token),
]
