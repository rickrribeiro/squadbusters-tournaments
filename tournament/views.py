from django.shortcuts import render, get_object_or_404
from tournament.utils import get_tournament_scores, get_table_template
from .models import Tournament

def tournament_details(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)
    player_scores = get_tournament_scores(tournament_id)
    print(tournament.table_header_name)
    template = get_table_template(tournament.tournament_type)
    
    context = {
        "tournament": {
            "id": tournament.id,
            "name": tournament.name,
            "type": tournament.tournament_type,
            "clan1": tournament.clan1.name if tournament.clan1 else "N/A",
            "clan2": tournament.clan2.name if tournament.clan2 else "N/A",
            "date": tournament.date,
            "table_header_name": tournament.table_header_name,
        },
        "player_scores": player_scores,
    }

    return render(request, template, context)

def tournament_list(request):
    tournaments = Tournament.objects.all()
    
    context = {
        "tournaments": tournaments
    }

    return render(request, "tournament_list.html", context)
