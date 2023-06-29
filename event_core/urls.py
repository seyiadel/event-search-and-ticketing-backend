"""
URL configuration for event_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="PassMaster API v1.0",
      default_version='v1.0',
      description="Event Ticketing API: Create Organization, Events, Tickets and Sell Tickets",
      terms_of_service="https://www.github.com/seyiadel",
      contact=openapi.Contact(email=""),
      license=openapi.License(name="MIT License"),
   ),
   url='https://event-ticketing-test-link-production.up.railway.app/',
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('event_app.urls')),
    path("", include('ticket_app.urls')),
    path("", include('payments.urls')),
    path("",include('organizations.urls')),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
