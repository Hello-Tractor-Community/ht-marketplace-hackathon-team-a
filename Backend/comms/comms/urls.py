"""
URL configuration for comms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include , re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Hello Tractor ",
        default_version='v1',
        description="List of api Hello Tractor Marketplace",
        
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('swagger.json./', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('swagger-yaml/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # Swagger JSON
    path('swagger-json/', schema_view.without_ui(cache_timeout=0), name='schema-swagger-json'),

    # Swagger YAML
    # path('swagger-yaml/', schema_view.without_ui(renderer_classes=[openapi.renderers.OpenAPIRenderer, openapi.renderers.YAMLOpenAPIRenderer]), name='schema-swagger-yaml'),

    
    # API Endpoints in setting.py
    path('cart/', include('cart.urls')),
    path('payments/', include('payments.urls')),
    path('users/', include('users.urls')),
    path('favorites/', include('favorites.urls')),
    # path('auth/', include('social_django.urls', namespace='social')),
    path('implements/', include('implements.urls')),
    path('usedTractors/', include('usedTractors.urls')),
    path('tractors/', include('tractors.urls')),
    path('messaging/', include('messaging.urls')),




]
