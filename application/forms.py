from django import forms
from .models import *

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = (
                  'home_team',
                  'guest_team',
                  'field',
                  'referee',
                  'referee_uid',
                  'start_time',
                  'home_team_score',
                  'guest_team_score',
                  'match_notes',
                  'match_players_goals_scored',)

class ModelForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = (
                  'home_team',
                  'guest_team',
                  'field',
                  'referee',
                  'start_time',
                  'home_team_score',
                  'guest_team_score',
                  'match_notes',
                  'match_players_goals_scored')

