from django.conf.urls import url
from django.views.generic import TemplateView

from . import views
from django.urls import path, re_path

app_name = 'application'
urlpatterns = [
    re_path(r'^home/$', views.home, name='home'),
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('match_list', views.match_list, name='match_list'),
    path('team_list', views.team_list, name='team_list'),

]
