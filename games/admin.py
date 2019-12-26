from django.contrib import admin
from games.models import GameCategory, Game

# Register your models here.
class GameCategoryAdmin(admin.ModelAdmin):
  pass

class GameAdmin(admin.ModelAdmin):
  pass

admin.site.register(GameCategory,  GameCategoryAdmin)
admin.site.register(Game, GameAdmin)

