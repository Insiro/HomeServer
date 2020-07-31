from django.urls import path
from . import views, api

urlpatterns = [
    path("", api.api, name="api"),
    path("todayCyphers", api.todayCyphers),
    path("UserID/name=<name>", api.getUserID),
    path("charRank/char=<charname>", api.charRank),
    path("userInfo/name=<name>", api.getUserInfo),
    path("allRanking/<args>", api.allRanking),
    path("allRanking", api.allRank),
    path("rating/<args>", api.rating),
]
