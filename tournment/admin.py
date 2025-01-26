from django.contrib import admin
from .models import Clan, Player, Tournment, TournmentMatch, PlayerMatch, PointsFormat

class PlayerMatchInline(admin.TabularInline):
    model = PlayerMatch
    extra = 10
    max_num = 10
    fields = ( "position","player", "gems", "killed_by")
    autocomplete_fields = ("player", "killed_by")
    

@admin.register(Clan)
class ClanAdmin(admin.ModelAdmin):
    list_display = ("name", "logo")
    search_fields = ("name",)


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("nick", "clan")
    search_fields = ("nick",)
    list_filter = ("clan",)


@admin.register(Tournment)
class TournmentAdmin(admin.ModelAdmin):
    list_display = ("name", "tournment_type", "clan1", "clan2", "date", "pointsFormat")
    search_fields = ("name",)
    list_filter = ("tournment_type", "date")


@admin.register(TournmentMatch)
class TournmentMatchAdmin(admin.ModelAdmin):
    list_display = ("tournment", "date")
    search_fields = ("tournment__name",)
    list_filter = ("date",)
    inlines = [PlayerMatchInline]

@admin.register(PlayerMatch)
class PlayerMatchAdmin(admin.ModelAdmin):
    list_display = ("player", "tournment_match", "gems", "killed_by", "clan")
    search_fields = ("player__nick", "tournment_match__tournment__name")
    list_filter = ("clan",)


@admin.register(PointsFormat)
class PointsFormatAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "points1",
        "points2",
        "points3",
        "points4",
        "points5",
        "points6",
        "points7",
        "points8",
        "points9",
        "points10",
        "points_per_kill",
        "lost_points_per_death",
    )
    search_fields = ("name",)
