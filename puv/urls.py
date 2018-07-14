from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^jsonData/$', views.getJSONData, name='getJSONData')
]
