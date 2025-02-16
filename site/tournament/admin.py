from django.contrib import admin
from .models import Tournament, TournamentMatch, PlayerMatch, PointsFormat

class PlayerMatchInline(admin.TabularInline):
    model = PlayerMatch
    extra = 10
    max_num = 10
    fields = ( "position","player", "gems", "killed_by")
    autocomplete_fields = ("player", "killed_by")
    


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    # list_display = ("name", "tournament_type", "clan1", "clan2", "date", "pointsFormat")
    search_fields = ("name",)
    list_filter = ("tournament_type", "date")
    autocomplete_fields = ("clan1","clan2")


@admin.register(TournamentMatch)
class TournamentMatchAdmin(admin.ModelAdmin):
    list_display = ("tournament", "date")
    search_fields = ("tournament__name",)
    list_filter = ("date",)
    inlines = [PlayerMatchInline]

@admin.register(PlayerMatch)
class PlayerMatchAdmin(admin.ModelAdmin):
    list_display = ("player", "tournament_match", "gems", "killed_by", "clan")
    search_fields = ("player__nick", "tournament_match__tournament__name")
    list_filter = ("clan",)
    autocomplete_fields = ("player","killed_by",)


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
