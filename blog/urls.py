"""myblog URL Configuration

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

from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^article/(?P<article_id>[0-9]+)/$', views.article_page, name='article_page'),
    url(r'^edit_page/(?P<article_id>[0-9]+)/$', views.edit_page, name='edit_page'),
    url(r'^edit_page/action$', views.article_new, name='article_new'),
    url(r'^dele_page/(?P<article_id>[0-9]+)/$', views.article_dele, name='dele_page'),
]
