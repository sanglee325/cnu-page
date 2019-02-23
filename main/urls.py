from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('manage', views.manage, name='manage'),
    path('contact', views.contact, name='contact'),
    #url(r'^logout/$', views.logout, name='logout'),
    #url(r'^signup/$', views.signup, name='signup'), #only signup page ready
]