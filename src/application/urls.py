"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.contrib.auth import decorators
from miptoverflow.views import HomePage, SearchQuestion, AskQuestion, UserSettings, UserQuestion, AboutPage, SignIn, SignUp

urlpatterns = [
    url(r'^$', HomePage.as_view(), name='home'),
    url(r'^search$', SearchQuestion.as_view(), name='search'),
    url(r'^question$', UserQuestion.as_view(), name='question'),
    url(r'^ask_question$', AskQuestion.as_view(), name='ask_question'),
    url(r'^settings$', UserSettings.as_view(), name='settings'),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}, name='logout'),
    url(r'^signin$', SignIn.as_view(), name='signin'),
    url(r'^signup$', SignUp.as_view(), name='signup'),
    url(r'^about$', AboutPage.as_view(), name='about'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
]
