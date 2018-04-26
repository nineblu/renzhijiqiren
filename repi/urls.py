from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^che/$', views.che, name='che'),
    url(r'^$', views.che, name='che'),
]