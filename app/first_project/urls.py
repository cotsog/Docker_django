"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        path('admin/', admin.site.urls),
    ]
    urlpatterns += [
        # path('__debug__/', include(debug_toolbar.urls)),
        path('polls/', include('polls.urls')),
        # path('blog/', include('blog.urls')),
        path('catalog/', include('catalog.urls'))
    ]
    # Add Django site authentication urls (for login, logout, password management)
    urlpatterns += [
        path('accounts/', include('django.contrib.auth.urls')),
        path('signup/', views.signup),
        path('register/', views.Register.as_view(), name="register"),
    ]
    #Add Django site authentication urls (for login, logout, password management)
