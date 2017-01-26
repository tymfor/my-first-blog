"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout_then_login
from django.conf.urls.static import static
from django.conf import settings


admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/login/$', auth_views.login, name = 'login'),
    url(r'^account/logout/$',lambda request: logout_then_login(request, "/"), name = 'logout'),
    url(r'', include('blog.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'', include('qna.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
