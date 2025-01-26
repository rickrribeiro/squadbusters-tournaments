from collections import defaultdict
from tournment.models import Player, PlayerMatch, Tournment


def get_kill_count_in_tournament(player_id, tournament_id):
    """Retorna o número de kills de um jogador em um torneio específico."""
    return PlayerMatch.objects.filter(
        killed_by=player_id,
        tournment_match__tournment=tournament_id
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
    tournament = Tournment.objects.get(id=tournament_id)
    points_format = tournament.pointsFormat

    player_data = PlayerMatch.objects.filter(tournment_match__tournment=tournament)

    ranking = defaultdict(lambda: {'gems': 0, 'deaths': 0, 'points': 0, 'kills': 0})

    for data in player_data:
        player_nick = data.player.nick
        was_killed = int(data.killed_by is not None)
        position = data.position

        points = get_points_for_position(position, points_format)
        points += was_killed * points_format.lost_points_per_death

        ranking[player_nick]['gems'] += data.gems
        ranking[player_nick]['deaths'] += was_killed
        ranking[player_nick]['points'] += points

    for player_nick in ranking:
        player = Player.objects.get(nick=player_nick)
        kills = get_kill_count_in_tournament(player.id, tournament_id)
        ranking[player_nick]['kills'] = kills
        ranking[player_nick]['points'] += kills * points_format.points_per_kill

    return ranking
