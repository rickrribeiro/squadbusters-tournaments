from collections import defaultdict
from django.db.models import Max, F
from .models import Record

def get_top_records():
    records = Record.objects.values('record_type__name', 'date', 'player__nick').annotate(max_value=Max('value'))
    
    record_dict = defaultdict(lambda: {'value': 0, 'players': []})
    
    for record in records:
        record_type_name = record['record_type__name']
        value = record['max_value']
        nick = record['player__nick']
        date = record['date']
        
        if value > record_dict[record_type_name]['value']:
            record_dict[record_type_name] = {'value': value, 'players': [nick], 'date': date}
        elif value == record_dict[record_type_name]['value']:
            record_dict[record_type_name]['players'].append(nick)
    
    result = [
        {
            'record_type': record_type_name,
            'date': data['date'],
            'player': ', '.join(data['players']),
            'value': data['value']
        }
        for record_type_name, data in record_dict.items()
    ]
    
    return result
