"""
URL configuration for api_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

API_TITLE = 'Simple API Service for Customers and Orders'
API_DESCRIPTION = 'A Web API for creating, modifying and deleting Customers and Orders'
version='1.0.0'
swagger_schema_view = get_swagger_view(title=API_TITLE)
docs_schema_view = get_schema_view(title=API_TITLE,
                                   description=API_DESCRIPTION,
                                   version=version)

urlpatterns = [
    path('admin/', admin.site.urls),
    # include urls for auhentication with mozilla-django-oidc
    path('api/v1/api-auth/', include('mozilla_django_oidc.urls')),
    path('api/v1/', include('api.urls')),
    #path('api/schema', docs_schema_view, name='schema-view'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    #path('api/docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    # path('api/swagger-docs/', swagger_schema_view, name='swagger-docs'),
    path('api/schema/swagger-docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
