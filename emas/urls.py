"""emas URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from user_site import views
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('user_site/', include('user_site.urls')),
    path('admin/', admin.site.urls),
    path('error_category/', views.error_category, name='error_category'),
    path('error_appearance/<str:location>', views.error_appearance, name='error_appearance'),
    path('solution/', views.solution, name='solution'),
    path('success/', views.success, name='success'),
    path('request_comment/', views.request_comment, name='request_comment'),
    path('edit_comment/', views.edit_comment, name='edit_comment'),
    path('pdf_locations/<str:location>', views.pdf_locations, name="pdf_locations"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


