from collections import defaultdict
from tournament.models import PlayerMatch, Tournament
from core.models import Player

def get_kill_count_in_tournament(player_id, tournament_id):
    """Retorna o número de kills de um jogador em um torneio específico."""
    return PlayerMatch.objects.filter(
        killed_by=player_id,
        tournament_match__tournament=tournament_id
    ).count()


def get_points_for_position(position, points_format):
    """Retorna os pontos com base na posição do jogador."""
    points_mapping = {
        1: points_format.points1,
        2: points_format.points2,
        3: points_format.points3,
        4: points_format.points4,
        5: points_format.points5,
        6: points_format.points6,
        7: points_format.points7,
        8: points_format.points8,
        9: points_format.points9,
        10: points_format.points10
    }
    return points_mapping.get(position, 0)


def get_tournament_scores(tournament_id):
    """Retorna os resultados de um torneio com pontos e estatísticas dos jogadores."""
    tournament = Tournament.objects.get(id=tournament_id)
    points_format = tournament.pointsFormat

    player_data = PlayerMatch.objects.filter(tournament_match__tournament=tournament)

    ranking = defaultdict(lambda: {'gems': 0, 'deaths': 0, 'points': 0, 'kills': 0})

    for data in player_data:
        player_nick = data.player.nick
        was_killed = int(data.killed_by is not None)
        position = data.position

        points = get_points_for_position(position, points_format)
        points += was_killed * points_format.lost_points_per_death

        ranking[data.player.id]['gems'] += data.gems
        ranking[data.player.id]['deaths'] += was_killed
        ranking[data.player.id]['points'] += points

    for player_id in ranking:
        player = Player.objects.get(id=player_id)
        kills = get_kill_count_in_tournament(player.id, tournament_id)
        ranking[player.id]['kills'] = kills
        ranking[player.id]['points'] += kills * points_format.points_per_kill
        ranking[player.id]['nick'] = player.nick
    
    new_data = {
    1: {'points': 88, 'kills': 1, 'gems': 5062},
    8: {'points': 84, 'kills': 1, 'gems': 4651},
    4: {'points': 77, 'kills': 2, 'gems': 4155},
    5: {'points': 74, 'gems': 3410},
    11: {'points': 49, 'kills': 1, 'gems': 3093},
    6: {'points': 38, 'gems': 2160},
    2: {'points': 35, 'gems': 1599},
    12: {'points': 16, 'gems': 795},
    7: {'points': 11, 'gems': 458}
}

    for player_id, data in new_data.items():
        if player_id in ranking:
            ranking[player_id]['gems'] += data.get('gems', 0)
            ranking[player_id]['points'] += data.get('points', 0)
            ranking[player_id]['kills'] += data.get('kills', 0)
    players_array = list(ranking.values())
    return sorted(players_array, key=lambda x: x['points'], reverse=True)


def get_table_template(tournament_type):
    """Retorna o template de tabela baseado no tipo de torneio."""
    if tournament_type == 'LBSB':
        return 'lbsb_table.html'
    return "tournament_details.html"