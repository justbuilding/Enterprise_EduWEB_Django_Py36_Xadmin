"""xadmin_django URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from message.views import get_form

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # ^表示以from开头，$表示以/结尾,逗号后面需先到migrations的views里写好view,记得from message.views import get_form
    # 记得逗号后的get_form不需要括号
    url(r'^form/$', get_form)
]
