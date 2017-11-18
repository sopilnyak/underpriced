from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from core.database import get_client
from ml_module.estimate_flat import estimate_flat

client = get_client()
db = client.underpriced
flats = db.flats


# Pages
def index(request):

    return render(request, 'index.html')

def get_flat(request, id):
    flat = flats.find_one({'_id': id})
    if flat is None:
        flat = {}
    return JsonResponse(flats)

def get_flat_list(request):
    flat_list = list(flats.find())
    return JsonResponse(flat_list)

def estimate_flat(request):
    if request.method == "POST":
        fields = [
            'area',
            'combined_bathroom_count',
            'construction_year',
            'house_type',
            'kitchen_area',
            'living_area',
            'repair',
            'rooms',
            'underground',
            'has_balcony',
            'has_loggia',
            'curr_floor',
            'total_floor'
        ]
        flat = {field: request.POST[field] for field in fields}
        price = estimate_flat(*flat)
        return JsonResponse({'price': price})
    else:
        return HttpResponseBadRequest()


# def usernames(request):
#
#     return JsonResponse(get_usernames(), safe=False)
