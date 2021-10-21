from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from .forms import *

def home(request):
    return render(request, 'home.html',)

def match_list(request):
    match = Match.objects.filter(created_date__lte=timezone.now())
    return render(request, 'match_list.html',
                 {'matches': match})

@login_required
def team_list(request):
    team = Team.objects.filter(created_date__lte=timezone.now())
    return render(request, 'team_list.html',
                 {'teams': team})

@login_required
def player_list(request):
    player = Player.objects.filter(created_date__lte=timezone.now())

    return render(request, 'player_list.html',
                 {'players': player})
