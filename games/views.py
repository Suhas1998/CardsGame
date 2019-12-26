from django.shortcuts import render
from games.models import GameCategory, Game

# Create your views here.
def games_index(request):
  games = Game.objects.all().order_by('name')
  context = {
    "games": games,
  }

  return render(request, 'games_index.html', context)

