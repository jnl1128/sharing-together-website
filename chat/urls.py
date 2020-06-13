from django.conf.urls import url
from . import views

app_name = 'chat'

urlpatterns = [
    url(r'^$', views.be_together, name='be_together'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]