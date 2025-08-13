from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_GET
from django.http import JsonResponse

@require_GET
def menu_list(request):
    menues = [
        {"name":"Espresso","price":3000},
        {"name":"Long Black","price":4000},
        {"name":"Vanila latte","price":5000},

    ]
    return JsonResponse(menues, safe=False)