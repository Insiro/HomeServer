"""CyphersChat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import cyphers.views
import cyphers.api
import home.views
import epic7.api
import epic7.views
import epic7.outApi

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api', include('cyphers.api')),
    path('', home.views.index),
    path('index', home.views.index),
    path('info', home.views.info),
    path('project', home.views.project),
    path('detail', home.views.detail),
    path('blank', home.views.blank),
    path('contact', home.views.contact),
    path('blog', home.views.blog),
    path('404', home.views._404),
    path('elem', home.views.elem),
    path('#', home.views.index),
    path('search', home.views.search),
    # Cyphers
    path('api/', cyphers.api.api, name='api'),
    path('api/todayCyphers', cyphers.api.todayCyphers),
    path('api/UserID/name=<name>', cyphers.api.getUserID),
    path('api/charRank/char=<charname>', cyphers.api.charRank),
    path('api/userInfo/name=<name>', cyphers.api.getUserInfo),
    path('api/allRanking/<args>', cyphers.api.allRanking),
    path('api/allRanking', cyphers.api.allRank),
    path('api/rating/<args>', cyphers.api.rating),
    # epic7
    path('epic/', epic7.views.index),
    path('epic/index', epic7.views.index),
    path('epic/tips', epic7.views.tiplit),
    path('epic/search', epic7.views.search),
    path('epic/notic', epic7.views.notic),
    path('epic/post', epic7.views.post),
    path('epic/damage', epic7.views.damageCalc),
    path('epic/detail', epic7.views.detail),
    # epic7API
    path('epic/info', epic7.api.info),
    path('epic/api/authorize', epic7.api.authorize),
    path('epic/api/isAuthrized', epic7.api.isAuthrized),
    # epicOutApi
    path('epic/api/getNotic', epic7.outApi.getNotic),
    path('epic/api/getReisterNotic', epic7.outApi.getReisterNotic),

]
