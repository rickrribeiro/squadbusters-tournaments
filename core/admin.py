from django.contrib import admin
from .models import Clan, Player
# Register your models here.

@admin.register(Clan)
class ClanAdmin(admin.ModelAdmin):
    list_display = ("name", "logo")
    search_fields = ("name",)


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("nick", "clan")
    search_fields = ("nick",)
    list_filter = ("clan",)
    autocomplete_fields = ("clan",)