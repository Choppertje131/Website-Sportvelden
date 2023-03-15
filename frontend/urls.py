from django.urls import path
from . import views

urlpatterns = [
path("login" ,views.loginview, name="login"),
path("logout", views.logoutview, name="logout"),
path("register", views.registerview, name="register"),
path("", views.homeview, name="home"),
path("veld1", views.veld1view, name="veld1"),
path("veld2", views.veld2view, name="veld2"),
path("settings", views.settingsview, name="settings"),
path("veld3", views.veld3view, name="veld3"),
path("veld4", views.veld4view, name="veld4"),
path("settingss", views.settingssview, name="settingss"),
]
