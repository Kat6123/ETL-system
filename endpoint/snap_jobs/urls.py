from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<location>\w*)$', views.index, name='index'),
]
