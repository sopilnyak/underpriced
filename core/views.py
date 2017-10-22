from django.shortcuts import render
from django.http import JsonResponse


# Pages
def index(request):

    return render(request, 'index.html')


# def usernames(request):
#
#     return JsonResponse(get_usernames(), safe=False)
