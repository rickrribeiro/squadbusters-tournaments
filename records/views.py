from django.shortcuts import render, get_object_or_404
from .utils import get_top_records


def record_list(request):
    records = get_top_records()
    
    context = {
        "records": records
    }

    return render(request, "record_list.html", context)
