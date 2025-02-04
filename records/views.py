from collections import defaultdict
from django.shortcuts import render, get_object_or_404
from .utils import get_top_records


def record_list(request):
    records = get_top_records()
    
    context = {
        "records": records
    }

    return render(request, "record_list.html", context)

def record_by_clan(request):
    records = get_top_records()
    
    records_by_clan = defaultdict()
    records_without_clan = []

    for record in records:
        print(record)
        if record["clans"]:
            for clan in record["clans"]:  # Se houver mais de um clã, podemos iterar sobre todos
                if clan not in records_by_clan:
                    records_by_clan[clan] = []
                records_by_clan[clan].append(record)
        else:
            records_without_clan.append(record)

    print(records_by_clan)
    context = {
        'records_by_clan': records_by_clan,
        'records_without_clan': records_without_clan,
    }

    return render(request, "record_by_clan.html", context)
