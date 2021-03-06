from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from core.database import get_client
from ml_module.estimate_flat import estimate_flat as ml_estimate_flat
import math

client = get_client()
db = client.underpriced
flats = db.flats
flat_limit = 500


# Pages
def index(request):
    return render(request, 'index.html')


def get_flat(request, id):
    flat = flats.find_one({'_id': id})
    if flat is None:
        flat = {}
    return JsonResponse(flats)


def get_underpriced_list(request):
    flat_list = list(flats.find({"$where": "this.estimated_price > this.price.rub_price && "
                                           "this.price.rub_price > 20000"}).limit(flat_limit))
    return JsonResponse(flat_list, safe=False)


def get_overpriced_list(request):
    flat_list = list(flats.find({"$where": "this.estimated_price < this.price.rub_price && "
                                           "this.price.rub_price > 20000"}).limit(flat_limit))
    return JsonResponse(flat_list, safe=False)


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
            'underground_name',
            'has_balcony',
            'has_loggia',
            'curr_floor',
            'total_floor',
            'underground_way',
            'underground_time',
        ]
        flat = {field: request.POST[field] if request.POST[field] != "" else None for field in fields}
        price = ml_estimate_flat(**flat)
        return JsonResponse({'price': price})
    else:
        return HttpResponseBadRequest()

# def usernames(request):
#
#     return JsonResponse(get_usernames(), safe=False)
