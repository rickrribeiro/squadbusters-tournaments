from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from tournment.utils import get_tournament_scores
from .models import Tournment, PlayerMatch

def tournment_details(request, tournment_id):
    tournment = get_object_or_404(Tournment, id=tournment_id)

    player_scores = get_tournament_scores(tournment_id)

    response_data = {
        "tournment": {
            "id": tournment.id,
            "name": tournment.name,
            "type": tournment.tournment_type,
            "clan1": tournment.clan1.name if tournment.clan1 else None,
            "clan2": tournment.clan2.name if tournment.clan2 else None,
            "date": tournment.date,
        },
        "player_scores": player_scores,
    }

    return JsonResponse(response_data)
