from django.urls import path
from . import views

urlpatterns = [
  path('', views.games_index, name= 'games_index'),
  path('<game>/', views.game_play, name= 'game_play')
]
