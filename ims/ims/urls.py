"""
URL configuration for ims project.

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
from django.urls import path, include
from authApp import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('', include('authApp.urls')),  # Set authApp as the root URL (homepage)
    path("accounts/login/", views.login_view, name="login"),  # Login page
    path("accounts/logout/", views.logout_view, name="logout"),  # Logout page
    path("accounts/register/", views.register_view, name="register"),  # Register page
    path('form_app/', include('form_app.urls')),  # Set form_app as the root URL (form_app)
    path('maininv/', include('maininv.urls')),  # maininv app at /maininv/
    path('inventory/', include('inventory.urls')),  # inventory app at /inventory/
]

