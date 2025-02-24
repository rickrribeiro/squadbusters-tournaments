import requests
from django.http import JsonResponse
import json

def external_info(request):
    player_id = request.GET.get('player_id')  # Pega o parâmetro da query string
    if player_id:
        url = f"https://boiling-brushlands-05108-5fd29f44600d.herokuapp.com/user/{player_id}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Lança um erro se o status não for 2xx
            data = response.json()
            
            formatted_chars = []
            rarity_map = {0: "comum", 1: "raro", 2: "épico"}
            parsed_response =  json.loads(data.get("jsonStr", {}))
            for char in parsed_response.get("chars", {}).get("c", []):
                formatted_chars.append({
                    "usecount": char.get("useCount"),
                    "name": char.get("Name"),
                    "rarity": rarity_map.get(char.get("Rarity"), "desconhecido"),
                    "total": int("".join(map(str, reversed(char.get("materialC", []))))),
                    "img": char.get("data")
                })
            res = {
                "chars": formatted_chars,
               # "next_chest":
            }
            return JsonResponse(res, safe=False)
        except requests.RequestException as e:
            return JsonResponse({'error': 'Erro ao buscar informações externas', 'details': str(e)}, status=500)
    
    return JsonResponse({'error': 'Parâmetro player_id não fornecido'}, status=400)
