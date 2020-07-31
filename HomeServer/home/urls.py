from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("index", views.index),
    path("info", views.info),
    path("project", views.project),
    path("detail", views.detail),
    path("blank", views.blank),
    path("contact", views.contact),
    path("blog", views.blog),
    path("404", views._404),
    path("elem", views.elem),
    path("#", views.index),
    path("search", views.search),
]
