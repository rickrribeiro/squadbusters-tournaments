from collections import defaultdict
from django.db.models import Max, Min
from .models import Record

def get_top_records():
    records = Record.objects.values(
        'record_type__name', 'date', 'player__nick', 'record_type__unity','player__clan__name', 'record_type__order_type'
    ).annotate(
        max_value=Max('value'),
        min_value=Min('value')
    )
    
    #clans is an array because there are group records ex pinhata group, duo, etc...
    record_dict = defaultdict(lambda: {'value': None, 'players': [], 'clans': set()})
    
    for record in records:
        record_type_name = record['record_type__name']
        order_type = record['record_type__order_type']
        value = record['max_value'] if order_type == 'biggest' else record['min_value']
        nick = record['player__nick']
        date = record['date']
        unity = record['record_type__unity']
        clan = record['player__clan__name']
        
        if record_dict[record_type_name]['value'] is None or \
           (order_type == 'biggest' and value > record_dict[record_type_name]['value']) or \
           (order_type == 'lowest' and value < record_dict[record_type_name]['value']):
            record_dict[record_type_name] = {'value': value, 'players': [nick], 'clans': {clan} if clan else set(), 'date': date, 'unity': unity}
        elif value == record_dict[record_type_name]['value']:
            record_dict[record_type_name]['players'].append(nick)
            if clan:
                record_dict[record_type_name]['clans'].add(clan)
    
    result = [
        {
            'record_type': record_type_name,
            'date': data['date'],
            'player': ', '.join(data['players']),
            'value': f"{data['value']} {data['unity'] or ''}".replace('.0', '').replace('.', ':'),
            'clans': data['clans']
        }
        for record_type_name, data in record_dict.items()
    ]
    
    return result