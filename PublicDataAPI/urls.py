from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework.permissions import AllowAny

# Swagger views with authentication disabled
schema_view = SpectacularAPIView.as_view(permission_classes=[AllowAny])
swagger_view = SpectacularSwaggerView.as_view(url_name='schema', permission_classes=[AllowAny])
redoc_view = SpectacularRedocView.as_view(url_name='schema', permission_classes=[AllowAny])

urlpatterns = [
    path('', include('apps.utility.urls')),
    path('api/public/health/', include('apps.health.urls')),
    path('api/public/', include('apps.public_api.urls')),

    # OpenAPI schema:
    path('api/public/schema/', schema_view, name='schema'),
    # Swagger UI:
    path('api/public/schema/swagger-ui/', swagger_view, name='swagger-ui'),
    # Redoc:
    path('api/public/schema/redoc/', redoc_view, name='redoc'),
    # Catch-all for undefined routes, redirect to root URL
    path('<path:slug>/', lambda request, slug: redirect('/')), 
]
