from django.conf.urls import url
from django.views.generic import TemplateView

from . import views
from django.urls import path, re_path

app_name = 'application'
urlpatterns = [
    re_path(r'^home/$', views.home, name='home'),
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('match_list', views.match_list, name='match_list'),
    path('match/<int:pk>/edit/', views.match_edit, name='match_edit'),
    path('team_list', views.team_list, name='team_list'),
    path('player_list', views.player_list, name='player_list'),
    path('player/<int:pk>/edit/', views.player_edit, name='player_edit'),
    path('player/create/', views.player_new, name='player_new'),

]
