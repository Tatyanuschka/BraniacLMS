from django.urls import path

from .apps import AuthappConfig
from .views import CustomLoginView, LogoutView, ProfileEditView, RegisterView

app_name = AuthappConfig.name

url_patterns = [
    path("login/", CustomLoginView.as_view, name="login"),
    path("register/", RegisterView.as_view, name="register"),
    path("logout/", LogoutView.as_view, name="logout"),
    path("edit/", ProfileEditView.as_view, name="edit"),
]
