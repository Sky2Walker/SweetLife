from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


def basket_adding(request):
    return_dict = dict

    session_key= request.session.session_key
    print(request.POST)
    return  JsonResponse(return_dict)