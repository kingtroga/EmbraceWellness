"""
URL configuration for ew project.

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
from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler403, handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('forum/', include('forum.urls')),
    path('blog/', include('blog.urls')),
    path('profile/', include('accounts.urls')),
    path('conversation/', include('conversation.urls')),
    path('direct_messages/', include('contact.urls')),
] 

handler404 = 'core.views.page_not_found'
handler403 = 'core.views.permission_denied'
handler500 = 'core.views.server_error'
