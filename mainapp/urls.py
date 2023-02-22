from django.urls import path, re_path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view(), name="main_page"),
    re_path("index", views.MainPageView.as_view(), name="main_page"),
    re_path("news", views.NewsPageView.as_view(), name="news"),
    path("news/<int:page>", views.NewsWithPaginatorView.as_view(), name="news_paginator"),
    re_path("courses", views.CoursesPageView.as_view(), name="courses"),
    re_path("contacts", views.ContactsPageView.as_view(), name="contacts"),
    re_path("doc_site", views.DocSitePageView.as_view(), name="doc_site"),
    re_path("login", views.LoginPageView.as_view(), name="login"),
]
