from django.urls import path
from . import views

# this path/url in browser, runs next function in views.py
urlpatterns = [
    path("<int:id>/", views.index, name="index"),
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create"),

]
