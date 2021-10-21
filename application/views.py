from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect


def home(request):
    return render(request, 'home.html',)

def match_list(request):
    match = Match.objects.filter(referee_uid=request.user)
    # match = Match.objects.filter(created_date__lte = timezone.now())
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

@login_required
def match_edit(request, pk):
    match = get_object_or_404(Match, pk=pk)
    print('here')
    print(match.pk)
    print(pk)
    if request.method == "POST":
        form = MatchForm(request.POST, instance=match)
        if form.is_valid():
            match = form.save()

            match.updated_date = timezone.now()
            match.save()
            matches = Match.objects.filter(referee_uid=request.user)
            return render(request, 'match_list.html', {'matches': matches})
    else:
        print("else")

        form = MatchForm(instance=match)
    return render(request, 'match_edit.html', {'form': form})

