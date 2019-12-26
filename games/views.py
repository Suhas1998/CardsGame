from django.shortcuts import render
from games.models import GameCategory, Game

# Create your views here.
def games_index(request):
  games = Game.objects.all().order_by('name')
  context = {
    "games": games,
  }
  return render(request, 'games/games_index.html', context)

def game_play(request, game):
  game = Game.objects.get(name=game)

  context = {
    "game" : game,
  }

  return render(request, "games/game_play.html", context)
