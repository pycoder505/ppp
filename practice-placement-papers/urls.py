import os
from django.conf.urls import patterns, include, url
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('database.urls', namespace="ppp"))
]