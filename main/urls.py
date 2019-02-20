from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    #url(r'^logout/$', views.logout, name='logout'),
    #url(r'^signup/$', views.signup, name='signup'), #only signup page ready
]