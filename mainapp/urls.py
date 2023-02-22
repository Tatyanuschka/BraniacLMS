from django.urls import path, re_path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view()),
    re_path("index", views.MainPageView.as_view()),
    re_path("news", views.NewsPageView.as_view()),
    re_path("courses", views.CoursesPageView.as_view()),
    re_path("contacts", views.ContactsPageView.as_view()),
    re_path("doc_site", views.DocSitePageView.as_view()),
    re_path("login", views.LoginPageView.as_view()),
]
