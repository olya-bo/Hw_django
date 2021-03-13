"""Hw_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path, include

from myapp.views import main_page, users, user, uuid_short, phone_number

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("myapp.urls")),
    path('users/', users, name='users'),
    path('users/<int:user_id>', user, name='user'),
    re_path(r'^(?P<phone>0(50|63|66|67|68|73|93|95|96|97|98|99)[0-9]{7})$', phone_number, name='phone_number'),
    re_path(r'^(?P<uuid>[a-f0-9]{4}-[a-f0-9]{6})$', uuid_short, name='uuid_short'),
]
