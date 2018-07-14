from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.userview, name='userview'),
    url(r'^userview/$', views.homeview, name='homeview'),
    url(r'^getUser2/$', views.storePickedStation, name='storePickedStation'),
    url(r'^userview2/$', views.userview2, name='userview2')
]
