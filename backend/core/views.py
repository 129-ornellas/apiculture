from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .forms import GetForm
import requests
import json

@require_http_methods(["GET"])
def get(request):
    form = GetForm.parse_obj(request.GET.dict())
    response = requests.get(form.url)
    data = json.dumps(response.json())
    return JsonResponse(data, status=response.status_code, safe=False)

@require_http_methods(["POST"])
def post(request):
    return JsonResponse({"post": 200})

@require_http_methods(["PUT"])
def put(request):
    return JsonResponse({"put": 200})

@require_http_methods(["PATCH"])
def patch(request):
    return JsonResponse({"patch": 200})

@require_http_methods(["DELETE"])
def delete(request):
    return JsonResponse({"delete": 200})
