from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^songs/$', views.ListSongs.as_view(), name='song-list'),
]