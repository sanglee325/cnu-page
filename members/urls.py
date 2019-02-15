from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('members', views.member, name='member'),
    #path('rsop2018/projects/<int:pk>', views.project, name='rsop-projects'),
    #path('rsop2018/projects/feedback/<int:pk>', views.project_feedback, name='rsop-project-feedback'),
]
