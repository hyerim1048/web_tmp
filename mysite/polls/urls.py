from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^foo/$', views.foo, name='foo'),
    re_path(r'^mygetview/$', views.mygetview, name='mygetview'),
    re_path(r'^mypostview/$', views.mypostview, name='mypostview'),
    re_path(r'^myajaxview/$', views.myajaxview, name='myajaxview'),
    re_path(r'^myajaxformview/$', views.myajaxformview, name='myajaxformview'),
]
