from django.shortcuts import render
from django.http import JsonResponse
from core.database import get_client

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


# def usernames(request):
#
#     return JsonResponse(get_usernames(), safe=False)
