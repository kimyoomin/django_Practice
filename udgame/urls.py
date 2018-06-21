from django.conf.urls import url
from . import views #.은 현재 폴더를 의미

urlpatterns = [
    url(r'^$', views.index), #위의 urls.py와는 달리 include가 없음
    url(r'^main$', views.index),
    url(r'^game$', views.game),
    url(r'^playing_game$', views.playing_game),
]
