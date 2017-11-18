from django.shortcuts import render
from django.http import JsonResponse
from pymongo import MongoClient

client = MongoClient('mongodb://underpriced:mongounderpriced@example.com/underpriced?authMechanism=SCRAM-SHA-1')

flats = client.flats


# Pages
def index(request):

    return render(request, 'index.html')

def get_flat(request, id):
    flat = flats.find_one({'_id': id})
    if flat is None:
        flat = {}
    return JsonResponse(flats)


# def usernames(request):
#
#     return JsonResponse(get_usernames(), safe=False)
