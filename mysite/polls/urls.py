from django.urls import path

from . import views

urlpatterns = [
    path('foo/', views.foo, name='foo'),
    path('mygetview/', views.mygetview, name='mygetview'),
    path('mypostview/', views.mypostview, name='mypostview'),
    path('myajaxview/', views.myajaxview, name='myajaxview'),
    path('myajaxformview/', views.myajaxformview, name='myajaxformview'),
]
